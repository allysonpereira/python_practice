import paho.mqtt.client as mqtt
import time

broker_address = "localhost"
port = 1883
topic = "test/topic"

client = mqtt.Client("P1")
client.connect(broker_address, port)

while True:
    message = "Hello!"
    ret = client.publish(topic, message)
    time.sleep(1)
