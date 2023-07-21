import boto3
import matplotlib.pyplot as plt
import pandas

dataLocalPath = "data.csv"

bucketName = 'inc-yashraj-training-eda'

s3Client = boto3.client('s3')

# Create bucket
location = {'LocationConstraint': 'ap-south-1'}
s3Client.create_bucket(Bucket=bucketName,
                        CreateBucketConfiguration=location)

# Push input file to bucket
with open(dataLocalPath, "rb") as f:
    s3Client.upload_fileobj(f, bucketName, "input/employeeData.csv")

# Read file
employeeDF = pandas.read_csv(dataLocalPath)

# Create Bar Chart
# Age vs Gender
plt.plot(employeeDF['Age'], employeeDF['Salary'])
plt.savefig('ageVsSalary.png')

# Push Output file to bucket
with open('ageVsSalary.png', "rb") as f:
    s3Client.upload_fileobj(f, bucketName, "output/ageVsSalary.png")
