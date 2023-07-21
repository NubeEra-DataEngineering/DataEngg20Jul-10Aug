import boto3

def upload_file(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name

    client.upload_file(file_name, bucket, object_name, ExtraArgs=args)

    print(f"'{file_name}' has successfully been uploaded to '{client}'")




AWS_REGION = "ap-south-1"
client = boto3.client("s3", region_name=AWS_REGION)
bucket_name = "bkt-taniya-assignment"
location = {'LocationConstraint': AWS_REGION}
#response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

upload_file(r'C:\Users\taniya.chauhan1\DataEngg20Jul-10Aug\TaniyaChauhan\Packages_Pandas\data.csv',bucket_name)
