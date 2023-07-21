import boto3
AWS_DEFAULT_REGION="ap-south-1"
s3Client=boto3.client("s3",region_name=AWS_DEFAULT_REGION)

allBuckets = s3Client.list_buckets()

for bucket in allBuckets['Buckets']:
    print(f' {bucket["Name"]}')