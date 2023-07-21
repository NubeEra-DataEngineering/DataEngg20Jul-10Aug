import boto3
import matplotlib.pyplot as plt
import pandas

dataLocalPath = "data.csv"
outputLocalPath = 'ageVsSalary.png'

bucketName = 'inc-yashraj-training-eda-3'

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
            self.s3Client.upload_fileobj(f, bucketName, f'{io}/{filePath}')

# s3Client = boto3.client('s3')

s3Helper = S3Driver(bucketName)

# Create bucket
s3Helper.create()

# Push input file to bucket
s3Helper.upload(dataLocalPath, io='input')

# Read file
employeeDF = pandas.read_csv(dataLocalPath)

# Create Bar Chart
# Age vs Gender
plt.plot(employeeDF['Age'], employeeDF['Salary'])
plt.savefig(outputLocalPath)

# Push Output file to bucket
s3Helper.upload(outputLocalPath, io='output')

