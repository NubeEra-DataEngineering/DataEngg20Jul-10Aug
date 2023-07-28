import boto3
import csv
import pymysql
import json

 

def lambda_handler(event, context):
    # AWS service clients
    s3_client = boto3.client('s3')
    rds_client = boto3.client('rds')
    sns_client = boto3.client('sns')

    # RDS database connection details
    rds_host = 'db-group-assignment2.ci9rghwaiseb.ap-south-1.rds.amazonaws.com'
    db_username = 'admin'
    db_password = 'admin123'
    db_name = 'asignement2DB'

    # S3 bucket and file details
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    # Retrieve the CSV file from S3
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        rows = response['Body'].read().decode('utf-8').splitlines()
        csv_reader = csv.reader(rows)

        # Connect to RDS database
        connection = pymysql.connect(host=rds_host,
                                     user=db_username,
                                     password=db_password,
                                     db=db_name,
                                     connect_timeout=5)
        cursor = connection.cursor()

        # Process and insert data into RDS database
        count = 0
        for row in csv_reader:
            # Assuming your CSV has columns 'column1', 'column2', 'column3'
            column1 = row[0]
            column2 = row[1]

            # Replace 'your_table_name' with the actual name of the table in the database
            sql = f"INSERT INTO tbl_ravali_crud (column1, column2) VALUES ('{column1}', '{column2}');"
            cursor.execute(sql)
            count += 1

        connection.commit()
        connection.close()

        # Send SNS notification
        sns_message = {
            'path': f's3://{bucket_name}/{file_key}',
            'count': count
        }

        sns_client.publish(
            TopicArn='arn:aws:sns:ap-south-1:475184346033:ravali-sns-assignment1',
            Message=json.dumps(sns_message),
            Subject='CSV Data Processing Report'
        )

        return {
            'statusCode': 200,
            'body': f'Successfully processed {count} records.'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }