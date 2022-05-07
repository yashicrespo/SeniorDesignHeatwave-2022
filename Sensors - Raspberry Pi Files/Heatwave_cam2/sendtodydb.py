# importing libraries
import paho.mqtt.client as paho
import boto3
import os
from pathlib import Path
import json
import socket
import ssl
import random
import string
import json
from datetime import datetime
from time import sleep
from random import uniform
 
connflag = False

access_key ='AKIAZD57QPO4PDLKTXFM'
secret_access_key ='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' 

client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)

#-----------------------------
 
def on_connect(client, userdata, flags, rc):                # func for making connection
    global connflag
    #print ("Connected to AWS")
    connflag = True
    #print("Connection returned result: " + str(rc) )
 
def on_message(client, userdata, msg):                      # Func for Sending msg
    print(msg.topic+" "+str(msg.payload))
    
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str
    
 
 
 
####-------sending flagged data
def mydynamodb(Id, flag,RoomTemp,PersonTemp):   
 mqttc = paho.Client()                                       # mqttc object
 mqttc.on_connect = on_connect                               # assign on_connect func
 mqttc.on_message = on_message                               # assign on_message func
 awshost = "a2icglxc0k8973-ats.iot.us-west-2.amazonaws.com"      # Endpoint
 awsport = 8883                                              # Port no.   
 clientId = "mything"                                     # Thing_Name
 thingName = "camwithdistSensor"                                    # Thing_Name
 caPath = "/home/pi/Videos/root-ca.pem"                                      # Root_CA_Certificate_Name
 certPath = "/home/pi/Videos/certificate.pem.crt"                            # <Thing_Name>.cert.pem
 keyPath = "/home/pi/Videos/private.pem.key"                          # <Thing_Name>.private.key
 mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters
 mqttc.connect(awshost, awsport, keepalive=60)               # connect to aws server
 mqttc.loop_start()                                          # Start the loop
 
 cat=0
 while cat==0:
    cat=1
    if connflag == True:
         
        CamId = 2
         
        today =datetime.today()
        d0=today.strftime("%m/%d/%y")
        now =datetime.now()
        t0=now.strftime("%H:%M:%S")
       
         
        paylodmsg0="{"                    #needed
        paylodmsg01 = "\"Id\":\""           #print st 1
        paylodmsg1  = "\",\"CamId\":\""        #print st 1
        
        
        paylodmsg2 = "\",\"Flag\":"        #print st 2
         
        paylodmsg3 = ",\"Time\":\""       #print st 3
        
        paylodmsg5 = "\",\"Days\":\""       #print st 5
        paylodmsg6 = "\",\"RoomTemp\":"   #print st 6
        paylodmsg7 = ",\"PersonTemp\":" #print st 7
        
        paylodmsg4= "}"                       # needed
        paylodmsg = "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(paylodmsg0, paylodmsg01, Id, paylodmsg1, CamId, paylodmsg2, flag, paylodmsg3, t0,paylodmsg5, d0, paylodmsg6, RoomTemp, paylodmsg7, PersonTemp, paylodmsg4)
        paylodmsg = json.dumps(paylodmsg) 
        paylodmsg_json = json.loads(paylodmsg)       
        mqttc.publish("Hem", paylodmsg_json , qos=1)        # topic: temperature # Publishing Temperature values
        print("msg sent: Hem" ) # Print sent temperature msg on console
        print(paylodmsg_json)
        
        file =open("wave1.txt","a")
        a0='[{"Id":'
        a2='}]'
        print(a0,a2)
        a1= a0+ str(Id) + ',"CamId":' + str(CamId) + ',"Flag":'+ str(flag) + ',"Date":"' + d0+ '","Time":"'+ t0 + '","PersonTemp":'+str(PersonTemp)+ ',"RoomTemp":'+ str(RoomTemp)+a2;
       # str1=repr(a1)
        a01=',{"Id":'
       
        a10= a01+ str(Id) + ',"CamId":' + str(CamId) + ',"Flag":'+ str(flag) + ',"Date":"' + d0+ '","Time":"'+ t0 + '","PersonTemp":'+str(PersonTemp)+ ',"RoomTemp":'+ str(RoomTemp)+a2;
       # str1=repr(a1)
        
        
        with open(r'wave1.txt', 'r') as file:
             data = file.read()
             data = data.replace(']', a10)
        with open(r'wave1.txt', 'w') as file:
            file.write(data)
           
    
        for file in os.listdir():
                if 'wave1.txt' in file:
                  upload_file_bucket ='imagetest23'
                  upload_file_key =str(file)
                   # upload_file_key ='python/' +str(file)
                  client.upload_file(file, upload_file_bucket, upload_file_key)
###-------------------
####--sending live data------
def livedb(Id,RoomTemp,PersonTemp):
 mqttc = paho.Client()                                       # mqttc object
 mqttc.on_connect = on_connect                               # assign on_connect func
 mqttc.on_message = on_message                               # assign on_message func
 awshost = "a2icglxc0k8973-ats.iot.us-west-2.amazonaws.com"      # Endpoint
 awsport = 8883                                              # Port no.   
 clientId = "mything"                                     # Thing_Name
 thingName = "camwithdistSensor"                                    # Thing_Name
 caPath = "/home/pi/Videos/root-ca.pem"                                      # Root_CA_Certificate_Name
 certPath = "/home/pi/Videos/certificate.pem.crt"                            # <Thing_Name>.cert.pem
 keyPath = "/home/pi/Videos/private.pem.key"                          # <Thing_Name>.private.key
 mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters
 mqttc.connect(awshost, awsport, keepalive=60)               # connect to aws server
 mqttc.loop_start()                                          # Start the loop
 
 cat=0
 while cat==0:
    cat=1
    if connflag == True:
         
        CamId = 2
         
        today =datetime.today()
        d0=today.strftime("%m/%d/%y")
        now =datetime.now()
        t0=now.strftime("%H:%M:%S")
       
         
        paylodmsg0="{"                    #needed
        paylodmsg01 = "\"Id\":\""           #print st 1
        paylodmsg1  = "\",\"CamId\":\""        #print st 1
        
        
        paylodmsg2 = ",\"Flag\":"        #print st 2
         
        paylodmsg3 = "\",\"Time\":\""       #print st 3
        
        paylodmsg5 = "\",\"Days\":\""       #print st 5
        paylodmsg6 = "\",\"RoomTemp\":"   #print st 6
        paylodmsg7 = ",\"PersonTemp\":" #print st 7
        
        paylodmsg4= "}"                       # needed
        paylodmsg = "{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(paylodmsg0, paylodmsg01, Id, paylodmsg1, CamId, paylodmsg3, t0,paylodmsg5, d0, paylodmsg6, RoomTemp, paylodmsg7, PersonTemp, paylodmsg4)
        paylodmsg = json.dumps(paylodmsg) 
        paylodmsg_json = json.loads(paylodmsg)       
        mqttc.publish("Live", paylodmsg_json , qos=1)        # topic: temperature # Publishing Temperature values
        print("msg sent: Live" ) # Print sent temperature msg on console
        print(paylodmsg_json)

                  

  