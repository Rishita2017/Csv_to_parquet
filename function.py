import boto3
import os
from botocore.exceptions import ClientError


def create_bucket(bucket_name, region='ap-south-1'):
    try:
        s3_client = boto3.client('s3', region_name=region)
        location = {'LocationConstraint': region}
        s3_client.create_bucket(Bucket=bucket_name,
                                CreateBucketConfiguration=location)

    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            print("Bucket already present")
        else:
            print(e)


def create_folder(bucket_name):
    try:
        s3_client = boto3.client('s3')
        s3_client.put_object(Bucket=bucket_name, Body='', Key='Read/')
        s3_client.put_object(Bucket=bucket_name, Body='', Key='Write/')
        print('Folder created successfully')
    except ClientError as e:
        print(e)


def upload_file(file_name, path, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)
        s3_client = boto3.client('s3')
        try:
            s3_client.upload_file(path, object_name)
        except ClientError as e:
            if e.response['Error']['Code'] == 'FileNotFoundError':
                print("File was not found")
            else:
                print(e)

