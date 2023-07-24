import boto3
AWS_DEFAULT_REGION="ap-south-1"
aws_access_key_id = 'AKIAW5IZRWOYQSLAZ3SL'
aws_secret_access_key = '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'
s3Client=boto3.client("s3",region_name=AWS_DEFAULT_REGION,aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,)

allBuckets = s3Client.list_buckets()

for bucket in allBuckets['Buckets']:
    print(f' {bucket["Name"]}')