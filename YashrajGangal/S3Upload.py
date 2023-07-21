import boto3

bucket_name = "inc-yashraj-trainingexample"

s3Client = boto3.client('s3')
with open("EmployeeClass.py", "rb") as f:
    s3Client.upload_fileobj(f, bucket_name, "sampleEmployeeFolder/EmployeeClass.py")
