import boto3

class S3Driver:
    def __init__(self, currentBucket) -> None:
        self.location = {'LocationConstraint': 'ap-south-1'}
        self.bucket = currentBucket
        self.s3Client = boto3.client('s3')
    
    def create(self):
        self.s3Client.create_bucket(Bucket=self.bucket,
                        CreateBucketConfiguration=self.location)
    
    def upload(self, filePath, io='output'):
        with open(filePath, "rb") as f:
            self.s3Client.upload_fileobj(f, self.bucket, f'{io}/{filePath}')