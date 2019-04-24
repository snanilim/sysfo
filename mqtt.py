import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#")

    # client.publish("house/main-light","OFF")
    # client.subscribe("house/main-light")
    # client.publish("house/main-light","ONN")

    msg = subscribe.simple("paho/test/simple", hostname="iot.eclipse.org")
    print("%s %s" % (msg.topic, msg.payload))
    publish.single("paho/test/single", "payload", hostname="iot.eclipse.org")
    
    

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client("p1")

client.on_connect = on_connect
client.on_message = on_message

client.message_retry_set(1)

client.connect("broker.hivemq.com")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()


# import paho.mqtt.client as mqtt #import the client1
# import time
# ############
# def on_message(client, userdata, message):
#     print("message received " ,str(message.payload.decode("utf-8")))
#     print("message topic=",message.topic)
#     print("message qos=",message.qos)
#     print("message retain flag=",message.retain)
# ########################################
# broker_address="broker.hivemq.com"
# #broker_address="iot.eclipse.org"
# print("creating new instance")
# client = mqtt.Client("P1") #create new instance
# client.on_message=on_message #attach function to callback
# print("connecting to broker")
# client.connect(broker_address) #connect to broker
# client.loop_start() #start the loop
# print("Subscribing to topic","house/bulbs/bulb1")
# client.subscribe("house/bulbs/bulb1")
# print("Publishing message to topic","house/bulbs/bulb1")
# client.publish("house/bulbs/bulb1","onn")
# time.sleep(10) # wait
# client.loop_forever() #stop the loop