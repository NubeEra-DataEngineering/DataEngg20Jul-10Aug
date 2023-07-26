# need help with setting up pandas in lambda environment

import json
import boto3
import csv
import pandas as pd
import logging

# dbHost = 'db-group-assignment2.ci9rghwaiseb.ap-south-1.rds.amazonaws.com'
# dbUser = 'admin'
# dbPassword = 'admin123'
# dbName = 'asignement2DB'

snsTopicARN = 'arn:aws:sns:ap-south-1:475184346033:sns-chiah-assign1'

def lambda_handler(event, context):
    bucketName = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    s3_client = boto3.client('s3')
    rds_client = boto3.client('rds-data')
    sns_client = boto3.client('sns')
    
    # read csv file from the bucket
    csv_file = s3_client.get_object(Bucket=bucketName, Key=key)['Body']
    
    # parse csv file
    df = pd.read_csv(csv_file)
    total_row = 0
    
    for _,row in df.iterrows():
        insert_into_rds(rds_client, row)
        total_row += 1
        
    # send sns message
    snsMessage = f"Path: s3://{bucketName}/{objectKey}\n"
    snsMessage += f"Counts: {total_rows}"
    sns.client.publish(TopicArn=snsTopicARN, Message=snsMessage)
    
    logger.info('Lambda function executed successfully')
    return 0
    
def insert_into_rds(rds_client, row):
    query = f"INSERT INTO tbl_chiah_crud (id, name) VALUES ({row['id']}, '{row['name']}');"
    response = rds_client.execute_statement(
        resourceArn='arn:aws:rds:ap-south-1:475184346033:db:db-group-assignment2',
        database=assignment2DB,
        sql=query
    )