import boto3

AWS_DEFAULT_REGION="ap-south-1"
aws_access_key_id = 'AKIAW5IZRWOYXX7ETXX7'
aws_secret_access_key = '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'
s3Client=boto3.client("s3",region_name=AWS_DEFAULT_REGION,aws_access_key_id=aws_access_key_id,

                  aws_secret_access_key=aws_secret_access_key,)
allBuckets = s3Client.list_buckets()
for bucket in allBuckets['Buckets']:

    print(f' {bucket["Name"]}')