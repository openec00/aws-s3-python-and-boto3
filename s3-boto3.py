#!/usr/bin/env python
# coding: utf-8

# In[1]:


import logging
import boto3
from botocore.exceptions import ClientError


# In[3]:


#Create S3 bucket - in a production systems you should avoid hard coding your AWS access and secret keys
AWS_ACCESS_KEY_ID = 'AKIAWS3UO4HZZVEZQ63U'
AWS_SECRET_ACCESS_KEY = '<AWS_SECRET_ACCESS_KEY>'

#Create a s3 client object
s3_client = boto3.client('s3', region_name ='eu-west-2',
                        aws_access_key_id = AWS_ACCESS_KEY_ID,
                        aws_secret_access_key = AWS_SECRET_ACCESS_KEY)

#Specify location of the s3 bucket using the Configuration parameter
location = {'LocationConstraint': 'eu-west-2'}

#Use the s3 client to create_bucket method to create a bucket
s3_client.create_bucket(Bucket = 'my-python-boto3-project',
                       CreateBucketConfiguration = location)


# In[4]:


# List Bucket on S3 with boto3 s3_client object 'list' method
bucket_list = s3_client.list_buckets()

for bucket in bucket_list['Buckets']:
    print(bucket['Name'])


# In[5]:


# Uploading files to a bucket with boto3 s3_client 'upload_file' method
file_name= 'Downloads/awesomecsv.csv'
bucket_name = 'my-python-boto3-project'
myfile = file_name

file_upload = s3_client.upload_file(file_name, bucket_name, myfile)


# In[8]:


# Uploading a file using the python file handler
with open(file_name, 'rb') as obj:
    s3_client.upload_fileobj(obj, bucket_name, 'Downloads/awesomecsv.clone.csv')


# In[9]:


# Upload file with ExtraArgs - enables you parse extra arguments when uploading a file
# Upload file with public read access
file_name= 'Downloads/awesomecsv.public.csv'
bucket_name = 'my-python-boto3-project'
myfile = file_name

file_upload = s3_client.upload_file(file_name, bucket_name, myfile,
                                   ExtraArgs={'ACL':'public-read'})


# In[10]:


# Downloading files
s3_client.download_file(bucket_name, 'Downloads/awesomecsv.clone.csv', 'Target/awesomecsv_download_target.csv')


# In[11]:


# Download and rename downloaded file using file handler (obj)
with open('Target/awesomecsv.copy.csv', 'wb') as obj:
    s3_client.download_fileobj(bucket_name, myfile, obj)


# In[ ]:




