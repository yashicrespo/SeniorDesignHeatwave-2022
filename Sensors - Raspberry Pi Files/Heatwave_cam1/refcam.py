import boto3
import os
import json
import time,board,busio
import numpy as np
import adafruit_mlx90640
import urllib3
import datetime
import plotly.express as px


def camref():
 i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
 mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
 mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate
 frame = np.zeros((24*32,)) # setup array for storing all 768 temperatures
 mlx_shape = (24,32)
 return mlx_shape
 