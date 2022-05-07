import boto3
import os
import json 
import time,board,busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
from scipy import ndimage
import PIL

#------------------------
access_key ='AKIAZD57QPO4PDLKTXFM'
secret_access_key ='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' 

client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)

#-----------------------------

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate
mlx_shape = (24,32) # mlx90640 shape

mlx_interp_val = 2 # interpolate # on each dimension
mlx_interp_shape = (mlx_shape[0]*mlx_interp_val,
                    mlx_shape[1]*mlx_interp_val) # new shape


def plot_update():
    fig = plt.figure(figsize=(12,9)) # start figure
    ax = fig.add_subplot(111) # add subplot
    fig.subplots_adjust(0.05,0.05,0.95,0.95) # get rid of unnecessary padding
    therm1 = ax.imshow(np.zeros(mlx_interp_shape),interpolation='none',
                       cmap=plt.cm.bwr,vmin=25,vmax=45) # preemptive image
    cbar = fig.colorbar(therm1) # setup colorbar
    cbar.set_label('Temperature [$^{\circ}$C]',fontsize=14) # colorbar label

    fig.canvas.draw() # draw figure to copy background
    ax_background = fig.canvas.copy_from_bbox(ax.bbox) # copy background
    fig.show() # show the figure before blitting

    frame = np.zeros(mlx_shape[0]*mlx_shape[1]) # 768 pts
    plt.ion() # enables interactive plotting
    fig.canvas.restore_region(ax_background) # restore background
    
    while True:
        #t1 = time.monotonic()
        try:
            
            mlx.getFrame(frame) # read mlx90640
            data_array = np.fliplr(np.reshape(frame,mlx_shape)) # reshape, flip data
            data_array = ndimage.zoom(data_array,mlx_interp_val) # interpolate
            therm1.set_array(data_array) # set data
            therm1.set_clim(vmin=np.min(data_array),vmax=np.max(data_array)) # set bounds
            cbar.on_mappable_changed(therm1) # update colorbar range
            plt.pause(0.0001) # required
           # plt.savefig('plot.jpg') # comment out to speed up
           # t_array.append(time.monotonic()-t1)
            PIL.Image.save('plot.jpg', compress_level=1)
             
            for file in os.listdir():
                if '.jpg' in file:
                  upload_file_bucket ='imagetest23'
                  upload_file_key =str(file)
                   # upload_file_key ='python/' +str(file)
                  client.upload_file(file, upload_file_bucket, upload_file_key)
                  #os.remove("plot.jpg")
             
            
            
            ax.draw_artist(therm1) # draw new thermal image
            fig.canvas.blit(ax.bbox) # draw background
            fig.canvas.flush_events() # show the new image
             
        except ValueError:
            continue # if error, just read again    
plot_update()