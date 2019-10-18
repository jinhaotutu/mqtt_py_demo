#!/usr/bin/env python
# encoding: utf-8
"""
@version: v1.0.0
@author: tutu
@license:
@contact:
@software: PyCharm
@file:
@time:
@describe: mqtt demo
"""

#import sys
#import os
import paho.mqtt.client as mqtt
import time

HOST = "127.0.0.1"
PORT = 1883
client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
mqtt_client = mqtt.Client("PY_Mqtt_Client-"+client_id, transport="tcp")
topic = "test"

def mqtt_connect():
    print("start connect mqtt-server")
    mqtt_client.username_pw_set("Hello world")

    mqtt_client.on_connect = mqtt_connected
    mqtt_client.on_log = mqtt_log

    mqtt_client.connect(HOST, PORT, 60)
    mqtt_client.loop_forever()

def sub_getmessage(client, userdata, msg):
    print(msg.topic + ":" + str(msg.payload))

def mqtt_connected(client, userdata, flags, rc):
    print("connecte succeed")
    mqtt_subscribe()

def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribe succeed")

def mqtt_subscribe():
    mqtt_client.subscribe(topic, 0)
    mqtt_client.on_message = sub_getmessage
    mqtt_client.on_subscribe = on_subscribe

def mqtt_log(client, userdata, level, buf):
    print(buf)

if __name__ == "__main__":
    mqtt_connect()
    while True:
        pass