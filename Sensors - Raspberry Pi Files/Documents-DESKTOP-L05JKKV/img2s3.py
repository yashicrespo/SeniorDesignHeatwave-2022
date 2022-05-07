import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import boto3
import io

# some random plotting. We need the figure object later
fig, ax = plt.subplots(1,1,figsize=(6,6))
ax.plot(np.linspace(0,1,50),
        np.random.normal(0.5,0.5,50))


canvas = FigureCanvas(fig) # renders figure onto canvas
imdata = io.BytesIO() # prepares in-memory binary stream buffer (think of this as a txt file but purely in memory)
canvas.print_png(imdata) # writes canvas object as a png file to the buffer. You can also use print_jpg, alternatively

s3 = boto3.resource('s3',
                    aws_access_key_id='AKIARUNMK4GUBMTIRJ34',
                    aws_secret_access_key='o+oQ46XSM3/q4Brb7NAE6YxCQ144Jdanwp3Vn06Q',
                    region_name='us-east-1') # or whatever region your s3 is in

s3.Object('yourbucket','picture.png').put(Body=imdata.getvalue(),
                                          ContentType='image/png') 
# this makes a new object in the bucket and puts the file in the bucket
# ContentType parameter makes sure resulting object is of a 'image/png' type and not a downloadable 'binary/octet-stream'

s3.ObjectAcl('yourbucket','picture.png').put(ACL='public-read')
# include this last line if you find the url for the image to be inaccessible