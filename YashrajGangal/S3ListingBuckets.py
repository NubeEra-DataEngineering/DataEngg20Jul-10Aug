import boto3

s3Client = boto3.client('s3')

allBuckets = s3Client.list_buckets()

for bucket in allBuckets["Buckets"]:
    print(f'{bucket["Name"]}')
