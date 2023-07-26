import pandas as pd
import matplotlib.pyplot as plt
import boto3
from io import BytesIO
df = pd.read_csv(r"C:\Users\ravali.satla\DataEngg20Jul-10Aug\Ravali\data.csv")
s3 = boto3.client(
    's3'
)
bucket_name = 'de-ravali-project3'
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration= {'LocationConstraint':'ap-south-1'})
data_file_s3_key = 'data/data1.csv'
s3.upload_file(r"C:\Users\ravali.satla\DataEngg20Jul-10Aug\Ravali\data.csv", bucket_name, data_file_s3_key)
s3_data = s3.get_object(Bucket=bucket_name, Key=data_file_s3_key)
df = pd.read_csv(s3_data['Body'])
plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
output_file = "age_distribution.png"
plt.savefig(output_file)
s3_file_key = 'eda_results/age_distribution.png'
with open(output_file, 'rb') as f:
    file_data = f.read()
s3.put_object(Bucket=bucket_name, Key=s3_file_key, Body=file_data)
