import boto3
import os
import json
#heatwave s3 bucket
access_key ='AKIAS3U7UNUBJL3SEVGZ'
secret_access_key ='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' 

client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)
for file in os.listdir():
    if '.py' in file:
        upload_file_bucket ='imagetest22'
        upload_file_key ='python/' +str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
        
 


#stat=client.describe_instance_status(IncludeAllInstances=True)

#with open("temp.txt","w") as f:
  #  json.dump(
  
#f = open("cmyfile.txt", "w")
 #upload_file_bucket = 'automateuploads3'
 #upload_file_key = 'test/' + str(text/temp.txt)
 #client.upload_file(temp.txt, upload_file_bucket, upload_file_key)
