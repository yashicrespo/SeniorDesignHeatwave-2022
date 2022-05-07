#workig prog for sending image and 
import boto3
import os
import json
import time,board,busio
import RPi.GPIO as GPIO
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
from matplotlib import cm
#------------------------
 # PINS MAPPING AND SETUP
# --------------------------------------------------------------------

echoPIN = 24
triggerPIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(echoPIN,GPIO.IN)
GPIO.setup(triggerPIN,GPIO.OUT)

#-----------------------------

i2c = busio.I2C(board.SCL, board.SDA, frequency=1000000) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate
frame = np.zeros((24*32,)) # setup array for storing all 768 temperatures
mlx_shape = (24,32)
mlx_interp_val = 10 # interpolate # on each dimension
mlx_interp_shape = (mlx_shape[0]*mlx_interp_val,
                    mlx_shape[1]*mlx_interp_val) # new shape
 
def video():
    # setup the figure for plotting
    plt.ion() # enables interactive plotting
    fig,ax = plt.subplots(figsize=(12,7))
    #therm1 = ax.imshow(np.zeros(mlx_interp_shape),interpolation='none',vmin=25,vmax=45,cmap=cm.coolwarm) #start plot with zeros
    therm1 = ax.imshow(np.zeros(mlx_interp_shape),interpolation='none',
                   cmap=plt.cm.bwr,vmin=25,vmax=45) # preemptive image
    cbar = fig.colorbar(therm1) # setup colorbar for temps
    cbar.set_label('Temperature [$^{\circ}$C]',fontsize=14) # colorbar label
    
    while True:

        try:
            mlx.getFrame(frame) # read MLX temperatures into frame var
            
            ##---------------------getting average of highest temp
            sorted_index_array = np.argsort(frame)
            sorted_array = frame[sorted_index_array]
#             print("Sorted array:", sorted_array)
#             break
            rslt = sorted_array[-25 : ]
             
            data_array = (np.reshape(frame,mlx_shape)) # reshape to 24x32
            therm1.set_data(np.fliplr(data_array)) # flip left to right
            therm1.set_clim(vmin=np.min(data_array),vmax=np.max(data_array)) # set bounds
            cbar.on_mappable_changed(therm1) # update colorbar range
            plt.pause(0.000001) # required
            #print (" Distance in ft: " + str(distance())+ "   ", end='\r')
            print (" Distance in ft: " + str(distance()))
            cat =distance()
            if cat <3 and cat>2:
                print("you are in between 1 ft and 3 feet from sensor: " + str(cat))
                print(" p see uu")

        except ValueError:
            continue # if error, just read again
#vid
def distance ():
 new_reading = False
 counter = 0
 distance = 0
 duration = 0

 # send trigger
 GPIO.output(triggerPIN, 0)
 time.sleep(0.000002)
 GPIO.output(triggerPIN, 1)
 time.sleep(0.000010)
 GPIO.output(triggerPIN, 0)
 time.sleep(0.000002)

 # wait for echo reading
 while GPIO.input(echoPIN) == 0:
   pass
   counter += 1
   if counter == 5000:
      new_reading = True
      break

 if new_reading:
    return False
 startT = time.time()

 while GPIO.input(echoPIN) == 1: pass
 feedbackT = time.time()

 # calculating distance
 if feedbackT == startT:
  distance = "N/A"
 else:
  duration = feedbackT - startT
  #soundSpeed/2 = 34300 /2*# cm/s* 0.0328084 ft/cm=562.66406
  distance = duration * 562.66406
  distance = round(distance, 1)
 time.sleep(0.1)
 return distance
##---------------------------------------- distance ---
video()


