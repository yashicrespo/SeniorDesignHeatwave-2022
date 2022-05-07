#from S3img.py import secrets_access_key, access_key

import boto3
import os
access_key ='AKIARUNMK4GUBMTIRJ34'
secret_access_key ='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'
client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)
for file in os.listdir():
    if '.py' in file:
        upload_file_bucket = 'mysabtest'
        upload_file_key = 'test/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)