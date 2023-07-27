import os
import boto3
import pandas as pd
import pymysql
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def send_sns_notification(subject, message):
    sns_client = boto3.client('sns')
    sns_topic_arn = 'arn:aws:sns:ap-south-1:475184346033:nithin_s3_topic'  
    sns_client.publish(TopicArn=sns_topic_arn, Subject=subject, Message=message)

def lambda_handler(event, context):
    
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_key = event['Records'][0]['s3']['object']['key']

    #RDS Details
    db_host = "db-group-assignment2.ci9rghwaiseb.ap-south-1.rds.amazonaws.com"
    db_username = "admin"
    db_password = "admin123"
    db_name = "db-group-assignment2"
    db_table_name = "tbl_nithin_crud"

    
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
    csv_content = response['Body']
    df = pd.read_csv(csv_content, skiprows=1)

    
    conn = pymysql.connect(host=db_host, user=db_username, passwd=db_password, db=db_name)
    cursor = conn.cursor()

    
    record_count = 0
    for index, row in df.iterrows():
        sql = f"INSERT INTO {db_table_name} (Id, Name) VALUES (%s, %s)"
        values = (row['Id'], row['Name'])
        cursor.execute(sql, values)
        record_count += 1
    
    conn.commit()
    cursor.close()
    conn.close()

    
    subject = "RDS Data Load Successful"
    message = f"Data from S3 bucket '{s3_bucket}/{s3_key}' successfully loaded into RDS table '{db_table_name}'.\nRecords inserted: {record_count}"
    send_sns_notification(subject, message)

    logger.info("CSV data loaded into RDS MySQL table successfully!")
    return {
        'statusCode': 200,
        'body': 'CSV data loaded into RDS MySQL table successfully!'
    }
