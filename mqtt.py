import sys
import os
import paho.mqtt.client as mqtt


HOST = "127.0.0.1"
PORT = 1883
mqtt_client = mqtt.Client()

def mqtt_connect():
    mqtt_client._client_id = "PY_Mqtt_Client"
    #mqtt_client.username_pw_set("Hello world")
    mqtt_client.connect(HOST, PORT, 60)
    mqtt_client.on_message = sub_getmessage
    #mqtt_client.on_connect = mqtt_connect
    mqtt_client.loop_forever()

def sub_getmessage(client, userdata, msg):
    print(msg.topic + ":" + str(msg.payload))

#def mqtt_connect():
    #mqtt_subscribe()

def mqtt_subscribe():
    mqtt_client.subscribe('test', 0)

if __name__ == "__main__":
    mqtt_connect()
    mqtt_subscribe()
    while True:
        pass