#workig prog for sending image and 
import boto3
import os
import json
import time,board,busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
#------------------------
 

#-----------------------------

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate
frame = np.zeros((24*32,)) # setup array for storing all 768 temperatures
mlx_shape = (24,32)

 
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
            
            
            
            
            data_array = (np.reshape(frame,mlx_shape)) # reshape to 24x32
            print(data_array)
            therm1.set_data(np.fliplr(data_array)) # flip left to right
            print(thermal)
            therm1.set_clim(vmin=np.min(data_array),vmax=np.max(data_array)) # set bounds
            
            cbar.on_mappable_changed(therm1) # update colorbar range
            plt.pause(0.0001) # required
            fig.savefig('plot.jpg',dpi=300,facecolor='#FCFCFC',bbox_inches='tight') # comment out to speed up
           # t_array.append(time.monotonic()-t1)
            
                   # upload_file_key ='python/' +str(file)
                              
            #print('Sample Rate: {0:2.1f}fps'.format(len(t_array)/np.sum(t_array)))
            #temp()
        except ValueError:
            continue # if error, just read again
#vid
video()


