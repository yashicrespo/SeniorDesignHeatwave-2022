import matrix
import distwidcam
import multiprocessing
import time
#workig prog for sending image and 
import boto3
import os
import json
import time,board,busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt

#------------------------
access_key ='AKIAZD57QPO4PDLKTXFM'
secret_access_key ='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' 

client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)

#-----------------------------
def cam():
 i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
 mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
 mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate
 frame = np.zeros((24*32,)) # setup array for storing all 768 temperatures
 mlx_shape = (24,32)
 plt.ion() # enables interactive plotting
 fig,ax = plt.subplots(figsize=(12,7))
 therm1 = ax.imshow(np.zeros(mlx_shape), interpolation='none',cmap=plt.cm.bwr,vmin=0,vmax=60) #start plot with zeros
 cbar = fig.colorbar(therm1) # setup colorbar for temps
 cbar.set_label('Temperature [$^{\circ}$C]',fontsize=14) # colorbar label
  
 while 1==1:
   
   
            mlx.getFrame(frame) # read MLX temperatures into frame var
            #frame =frame *(9.0/5.0)+32          
            data_array = (np.reshape(frame,mlx_shape)) # reshape to 24x32
            therm1.set_data(np.fliplr(data_array)) # flip left to right
            therm1.set_clim(vmin=np.min(data_array),vmax=np.max(data_array)) # set bounds
            cbar.on_mappable_changed(therm1) # update colorbar range
            plt.pause(0.0001) # required
            fig.savefig('plot1.jpg',dpi=300,facecolor='#FCFCFC',bbox_inches='tight') # comment out to speed up
          
            for file in os.listdir():
                if '.jpg' in file:
                  upload_file_bucket ='imagetest23'
                  upload_file_key =str(file)
                   # upload_file_key ='python/' +str(file)
                  client.upload_file(file, upload_file_bucket, upload_file_key)
            


def mat():   # sending matrix to create plot on website
    while 1==1:
        matrix.frame2db()

def distcam():
     
    while 1==1:
        distwidcam.loopp()
      
p1 = multiprocessing.Process(target=mat)
p2 = multiprocessing.Process(target=distcam)


p1.start()  
p2.start()
 
#cam()

