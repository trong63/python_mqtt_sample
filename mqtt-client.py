# -*- coding: utf-8 -*-
#BT - On the Conduit, type the following commands
#pip install paho-mqtt

import paho.mqtt.client as mqtt
import json



def on_connect(client, userdata, flags, rc):

	print("Connected with result code "+str(rc))
	client.subscribe("lora/+/up")


def on_message(client, userdata, msg):
	print("Topic: ", msg.topic+'\nMessage: '+str(msg.payload))
	#BT - Extract out the mac address in the topic
	mac_node = msg.topic.split('/')
	print("BT - mac_node: " + mac_node[1])
	#BT - Convert to json format data structure
	json_data = json.loads(msg.payload.decode("utf-8"))
	topic_down = "lora/" + mac_node[1] + "/down"
        print("BT - Topic down: " + topic_down)
	print("BT - json_data: %s" %(json_data["data"]))
	data_to_mDot = "{ \"data\": \"" + json_data["data"] + "\" }"
        print("BT - data_to_mDot: " + data_to_mDot)
	client.publish(topic_down,data_to_mDot)



client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)


client.loop_forever()


