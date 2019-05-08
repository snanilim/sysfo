from agent_info import *
import time
import paho.mqtt.client as mqtt
import random
import re, uuid
import json



uuid.uuid4 # generating randorm number in base64
r = str(uuid.uuid4())
client = mqtt.Client(r)
broker = "broker.hivemq.com"
port = 1883

mac_addr = mac_addr()
keep_alive = {
	'mac_addr': mac_addr,
	'alive': True
}
keep_alive = str(keep_alive)

division = None
district = None
upazilla = None
lab_id = None



def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))


def on_message(client, userdata, message):
	print("topic: "+message.topic+"	"+"payload: "+str(message.payload.decode("utf-8")))
	check_topic(str(message.payload.decode("utf-8")))
	send_data_to_broker(str(message.payload.decode("utf-8")))

client.on_connect = on_connect  #attach the callback function to the client object 
client.on_message = on_message	#attach the callback function to the client object



client.connect(broker,port,60)
print ("connecting to broker")


# client.subscribe("srdl/req_info/test")
client.subscribe(f"srdl/req_info/{division}/{district}/{upazilla}/{lab_id}/{mac_addr}/")
client.subscribe(f"srdl/res_topic/{mac_addr}", 1)
if district is None:
	client.publish(f"srdl/req_topic/{mac_addr}", str({"topic": 1}))
print ("subscribed", f"srdl/req_topic/{mac_addr}")


def check_topic(msg):
	global division, district, upazilla, lab_id
	if (division is None and district is None and upazilla is None and lab_id is None):
		data = json.loads(msg)
		topic_value = data.get("topic", "")

		if 'topic' in data and topic_value == 1:
			if 'division' in data:
				value = data.get("division", "")
				division = value
				print('msges', value)

			if 'district' in data:
				value = data.get("district", "")
				district = value
				print('msges', value)

			if 'upazilla' in data:
				value = data.get("upazilla", "")
				upazilla = value
				print('msges', value)

			if 'lab_id' in data:
				value = data.get("lab_id", "")
				lab_id = value
				print('msges', value)
		else:
			client.publish(f"srdl/req_topic/{mac_addr}", str({"topic": 1}))
		# print(f"srdl/req_topic/{mac_addr}")
		# district = "Dhaka"
	else:
		return True

def send_data_to_broker(msg):
	data = json.loads(msg)
	info_value = data.get("info", "")

	if 'info' in data and info_value == 1:
		print("I'm here")
		res_info = info(data)
		# print(res_info)
		client.publish(f"srdl/res_info/{division}/{district}/{upazilla}/{lab_id}/{mac_addr}", str(res_info))

	
	

client.loop_forever() # to maintain continuous network traffic flow with the broker


