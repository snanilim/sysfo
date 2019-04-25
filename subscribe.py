#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/test")

def on_message(client, userdata, message):
  topic = message.topic
  msgr = str(message.payload.decode("utf-8"))
  msgr = "Message Received " + msgr
  print(msgr)
    # client.disconnect()
    
client = mqtt.Client()
client.connect("broker.hivemq.com",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
