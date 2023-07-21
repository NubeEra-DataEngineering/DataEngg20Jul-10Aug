import logging
import boto3
from botocore.exceptions import ClientError
import os

import pandas as pd
from matplotlib import pyplot as plt

def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

    except ClientError as e:
        logging.error(e)
        return False
    return True

def upload_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def analyze(data):
    df = pd.read_csv(data)
    
    fig, ax = plt.subplots(nrows=1, ncols=2)
    ax[0].set_xticklabels(df['Name'],rotation=45)
    ax[0].bar(df['Name'], df['Salary'])
    ax[0].set_title('Salary Distribution')

    ax[1].set_xticklabels(df['Name'],rotation=45)
    ax[1].bar(df['Name'], df['Age'])
    ax[1].set_title('Age Distribution')


    plt.savefig('SumeetS/21Jul/output.png')



# Create Bucket
# create_bucket('sumeets-eda-21jul', 'ap-south-1')

# Upload Data
upload_file('SumeetS/data.csv', 'sumeets-eda-21jul', 'Data/eda.csv')

# Analyze
analyze('SumeetS/data.csv')

# Upload Result
upload_file('SumeetS/21Jul/output.png', 'sumeets-eda-21jul', 'Output/output.png')