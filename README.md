# pahoDjangoV2.0

A Django web application with integrated MQTT publishing capability using the Eclipse Paho library. Allows triggering MQTT messages from a web interface.

## Overview

This project combines a Django backend with an MQTT client module, enabling web-driven IoT control. HTTP requests to the Django app result in MQTT messages being published to a configured broker — useful for controlling devices or services over a local network.

## Tech Stack

| Component | Technology |
|-----------|------------|
| Web framework | Django |
| MQTT client | Eclipse Paho (`paho-mqtt`) |
| Language | Python 3 |

## Project Structure

```
projectDir/
  mqttClient/           # Django app for MQTT publishing
    mqtt_publish.py     # Core MQTT connect/publish/disconnect helpers
    views.py            # Django views that trigger MQTT publishes
    models.py           # Data models
    urls.py             # URL routing
  projectDir/
    settings.py
    urls.py
  manage.py
```

## Setup

1. Install dependencies:

```bash
pip install django paho-mqtt
```

2. Configure your MQTT broker settings in `mqttClient/mqtt_publish.py` and `mqttClient/views.py`:

```python
broker   = '<your_broker_ip>'
port     = 1883
username = '<your_username>'
password = '<your_password>'
```

3. Apply migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```

## Usage

Send an HTTP request to the configured endpoint — the Django view will connect to the MQTT broker, publish the message, and disconnect.

## License

MIT
