import matplotlib.pyplot as plt
import pandas
from s3Driver import S3Driver

dataLocalPath = "data.csv"
outputLocalPath = 'ageVsSalary.png'

bucketName = 'inc-yashraj-training-eda-5'

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

