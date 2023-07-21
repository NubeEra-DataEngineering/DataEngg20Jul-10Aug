import boto3

s3 = boto3.client('s3')

for bucket in s3.list_buckets()['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')
    

# with open("tmp123.csv", "rb") as f:
#     s3.upload_fileobj(f, "bkt-sumeetb-21july-1213pm", "tmp123.csv")

