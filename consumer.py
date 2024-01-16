import paho.mqtt.client as mqtt

#define the message callback function:
def on_message(client, userdata, message):
    print(f"Received message: {str(message.payload.decode('utf-8'))} on topic {message.topic}") #this function is called when a message is received. It prints the message payload and topic.

#setting up MQTT parameters:
broker_address = "localhost" 
port = 1883
topic = "test/topic" #these variables define the MQTT broker's address, port number, and the topic on which the consumer will subscribe.

#creating and configuring the MQTT client:
client = mqtt.Client("C1") 
client.on_message = on_message  
client.connect(broker_address, port) #the MQTT client is created with the ID "C1", and the on_message callback function is set. The client then connects to the MQTT broker.

#starting the client loop and subscribing to a topic
client.loop_start()  
client.subscribe(topic) #the client loop is started to handle incoming messages asynchronously, and it subscribes to the specified topic.

#running an infinite loop until interrupt:
try:
    while True:
        pass  
except KeyboardInterrupt:
    client.loop_stop()  
#The program enters an infinite loop to keep the script running. The loop can be terminated by pressing Ctrl+C, which triggers the KeyboardInterrupt exception, and the MQTT client loop is stopped.
