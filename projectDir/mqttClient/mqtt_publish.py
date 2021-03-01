import paho.mqtt.client as mqtt_client

broker = '192.168.1.4'
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


def publish(client, topic, msg):
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
    status = publish(client, topic, msg)
    disconnect_mqtt(client)
    return status
