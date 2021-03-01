from django.shortcuts import render
from django.http import HttpResponse
import paho.mqtt.client as mqtt_client

broker = '192.168.1.6'
port = 1883
client_id = 'test_ID_remote_admin'
username = 'sakib'
password = 'hd85512b'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def _publish(client, topic, msg):
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print(f"Sent `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
    return status

def disconnect_mqtt(client):
    client.disconnect()

def run_publish(topic, msg):
    client = connect_mqtt()
    status = _publish(client, topic, msg)
    disconnect_mqtt(client)
    return status



def home(request):
    return render(request, 'home.html', {'name' : 'Sakib'})


def publish(request):
    topic = request.POST['topic']
    msg = request.POST['message']
    status = run_publish(topic, msg)
    if status == 0:
        return render(request, 'home.html', {'name' : 'Sakib', 'msg': msg , 'topic' : topic})
    else:
        return render(request, 'home.html', {'name' : 'Sakib', 'msg': 'failed' , 'topic' : 'failed'})

def subscribe(request):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        message = msg.payload.decode()
    
    topic = request.POST['topic']
    message = ''
    client = connect_mqtt()
    client.subscribe(topic)
    client.on_message = on_message
    client.on_connect
    client = connect_mqtt()
    client.loop_start() 
    client.subscribe(topic)
    client.loop_stop() #stop the loop
    return render(request, 'subscribe.html', {'msg': message , 'topic' : topic})

