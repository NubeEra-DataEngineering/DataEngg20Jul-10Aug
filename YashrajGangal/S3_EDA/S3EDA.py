import matplotlib.pyplot as plt
import pandas
from s3Driver import S3Driver

dataLocalPath = "data.csv"
outputLocalPath = 'ageVsSalary.png'

bucketName = 'inc-yashraj-training-eda-6'

s3Helper = S3Driver(bucketName)

# Create bucket
s3Helper.create()

# Push input file to bucket
s3Helper.upload(dataLocalPath, io='input')

# Read file
employeeDF = pandas.read_csv(dataLocalPath)

print(f'Age Statistics:\nMin:{employeeDF.Age.min()}\tAverage:{employeeDF.Age.mean()}\tMax:{employeeDF.Age.max()}')
print(f'Salary Statistics:\nMin:{employeeDF.Salary.min()}\tAverage:{employeeDF.Salary.mean()}\tMax:{employeeDF.Salary.max()}')

# Create Bar Chart
# Age vs Gender
plt.plot(employeeDF['Age'], employeeDF['Salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs Salary Pattern')
plt.savefig(outputLocalPath)

# Push Output file to bucket
s3Helper.upload(outputLocalPath, io='output')

