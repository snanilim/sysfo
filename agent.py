from agent_pc_info import *
import time
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
keep_alive = {
	'mac_addr': mac_addr,
	'alive': True
}
keep_alive = str(keep_alive)


def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))

def on_publish(client, userdata, mid):
	# print('message')
	client.publish("web/hello", keep_alive)
	# time.sleep(10)

def on_message(client, userdata, message):
	# print(message.payload)
    print("topic: "+message.topic+"	"+"payload: "+str(message.payload.decode("utf-8")))
    send_data_to_broker(str(message.payload.decode("utf-8")))


   
  


client.on_connect = on_connect  #attach the callback function to the client object 
client.on_message = on_message	#attach the callback function to the client object
client.on_publish = on_publish


client.connect(broker,port,60)
print ("connecting to broker")


client.subscribe("srdl/req_info/test")
client.subscribe("srdl/each_info/{mac_addr}")
# client.subscribe("web/hello", 0)
# client.publish("web/hello", keep_alive)
print ("subscribed")

def send_data_to_broker(msg):
	msg_list = msg.split(',')
	print('msg', msg_list[0])

	if(msg_list[0] == '1'):
		
		print("I'm here")
		res_info = info(msg_list)
		# print(res_info)
		client.publish("srdl/info/test", str(res_info))

	
	if(msg_list[0] == '1'):
		from idle import get_idle_time
		print("Im not here")
		res_info = get_idle_time()
		print(res_info)
		client.publish("srdl/idle/test", str(res_info))
	

client.loop_forever() # to maintain continuous network traffic flow with the broker


