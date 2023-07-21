import boto3

s3_client = boto3.client('s3')

all_buckets = s3_client.list_buckets()

for bucket in all_buckets['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')