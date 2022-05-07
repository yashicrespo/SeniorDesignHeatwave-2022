#workig prog for sending image and 
import boto3
import os
import json
import time,board,busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
#------------------------
access_key ='AKIAS3U7UNUBJL3SEVGZ'
secret_access_key ='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' 

client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)

#-----------------------------

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate
frame = np.zeros((24*32,)) # setup array for storing all 768 temperatures
mlx_shape = (24,32)


# def temp():
#     while True:
#         try:
#             mlx.getFrame(frame) # read MLX temperatures into frame var
#             
#             c= open("temp.txt","w")
#             c.write("%s : %s\n" %("Current Temperature", frame))
#             c.close()
#             break
#         except ValueError:
#             continue # if error, just read again
# # print out the average temperature from the MLX90640
#     print('Average MLX90640 Temperature: {0:2.1f}C ({1:2.1f}F)'.\
#       format(np.mean(frame),(((9.0/5.0)*np.mean(frame))+32.0)))
# #print("array of temp : ", frame)  array of temp

def video():
    # setup the figure for plotting
    plt.ion() # enables interactive plotting
    fig,ax = plt.subplots(figsize=(12,7))
    therm1 = ax.imshow(np.zeros(mlx_shape),vmin=0,vmax=60) #start plot with zeros
    cbar = fig.colorbar(therm1) # setup colorbar for temps
    cbar.set_label('Temperature [$^{\circ}$C]',fontsize=14) # colorbar label


    #t_array = []
    while True:
        #t1 = time.monotonic()
        try:
            mlx.getFrame(frame) # read MLX temperatures into frame var
            
            
            c= open("temp.txt","w")
            c.write("%s : %s\n" %("Current Temperature : ", np.mean(frame)))
            c.close()
            c= open("array.txt","w")
            c.write(str(frame))
            c.close()
            
            data_array = (np.reshape(frame,mlx_shape)) # reshape to 24x32
            therm1.set_data(np.fliplr(data_array)) # flip left to right
            therm1.set_clim(vmin=np.min(data_array),vmax=np.max(data_array)) # set bounds
            cbar.on_mappable_changed(therm1) # update colorbar range
            plt.pause(0.0001) # required
            fig.savefig('plot.jpg',dpi=300,facecolor='#FCFCFC',bbox_inches='tight') # comment out to speed up
           # t_array.append(time.monotonic()-t1)
            for file in os.listdir():
                if '.jpg' in file:
                  upload_file_bucket ='imagetest22'
                  upload_file_key =str(file)
                   # upload_file_key ='python/' +str(file)
                  client.upload_file(file, upload_file_bucket, upload_file_key)
            for file in os.listdir():
                if '.txt' in file:
                  upload_file_bucket ='imagetest22'
                  upload_file_key =str(file)
                   # upload_file_key ='python/' +str(file)
                  client.upload_file(file, upload_file_bucket, upload_file_key)
            
            #print('Sample Rate: {0:2.1f}fps'.format(len(t_array)/np.sum(t_array)))
            #temp()
        except ValueError:
            continue # if error, just read again
#vid
video()

