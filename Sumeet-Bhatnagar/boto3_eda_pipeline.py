import boto3
import pandas as pd
import matplotlib.pyplot as plt

s3Client = boto3.client('s3')

bucket_name = 'bkt-sumeetb-eda-21jul-0415-3'


response = s3Client.create_bucket(

Bucket=bucket_name,
CreateBucketConfiguration={
    'LocationConstraint': 'ap-south-1'
    

},
  
)

print(response)


    
with open("./Packages_pandas/data.csv", "rb") as f:
    s3Client.upload_fileobj(f, bucket_name, "/input/data.csv")


df = pd.read_csv('./Packages_pandas/data.csv')

plt.bar(df.Name,df.Salary)
plt.xlabel('Employee names')
plt.ylabel('Salary')
plt.savefig('./employee_report.png')

with open("employee_report.png", "rb") as f:
    s3Client.upload_fileobj(f, bucket_name, "/Output/employee_report.png")






    


