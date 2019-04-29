from agent_pc_info import *

import paho.mqtt.client as mqtt
import random
import re, uuid 




uuid.uuid4 # generating randorm number in base64
r = str(uuid.uuid4())
client = mqtt.Client(r)
broker = "broker.hivemq.com"
port = 1883
mac_addr = hex(uuid.getnode()).replace('0x', '')
':'.join(mac_addr[i : i + 2] for i in range(0, 11, 2))


def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))

def on_message(client, userdata, message):
	# print(message.payload)
    print("topic: "+message.topic+"	"+"payload: "+str(message.payload.decode("utf-8")))
    send_data_to_broker(str(message.payload.decode("utf-8")))
   
  


client.on_connect = on_connect  #attach the callback function to the client object 
client.on_message = on_message	#attach the callback function to the client object


client.connect(broker,port,60)
print ("connecting to broker")


client.subscribe("srdl/req_info/test")
client.subscribe("srdl/each_info/{mac_addr}")
print ("subscribed")

def send_data_to_broker(msg):
	msg_list = msg.split(',')
	print('msg', msg_list[0])

	if(msg_list[0] == '1'):
		print("I'm here")
		res_info = info(msg_list)
		# print(res_info)
		client.publish("srdl/info/test", str(res_info))
	

client.loop_forever() # to maintain continuous network traffic flow with the broker


