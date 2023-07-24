import boto3

# Set up AWS credentials
aws_access_key_id = 'AKIAW5IZRWOYQSLAZ3SL'
aws_secret_access_key = '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'
region_name = 'ap-south-1'
s3 = boto3.client('s3',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  region_name=region_name)
bucket_name = 'de-ravali-project'
file_path = r'C:\Users\ravali.satla\DataEngg20Jul-10Aug\Ravali\data.csv'
object_key = 'data.csv'  # This will be the object name in S3

s3.upload_file(file_path, bucket_name, object_key)
