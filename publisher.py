import paho.mqtt.client as mqtt
import sys

def on_message(clinet, userdata , message):
    print(message.topic + ":" + message.payload.decode)

client = mqtt.Client()
client.on_message = on_message

if client.connect("localhost" , 1883) != 0:
    print("Could not connect to mqtt broker.")
    sys.exit(-1)

client.subscribe("test/topic")

try:
    print("Press CTRL+C to exit")
    client.loop_forever()
except:
    print("Disconnecting from broker")
    client.disconnect()