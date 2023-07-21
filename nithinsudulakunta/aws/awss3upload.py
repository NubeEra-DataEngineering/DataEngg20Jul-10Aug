
import boto3

s3 = boto3.client(
    's3'
)

for bucket in s3.list_buckets()['Buckets']:
    print(bucket['Name'])

local_file_path = 'C:/Users/nithin.sudulakunta/Downloads/TestReport.csv'
s3_bucket = 'bkt-nithinsai-21july2023'
current_path = 'sdk/TestReport'

s3.upload_file(local_file_path, s3_bucket, current_path)
