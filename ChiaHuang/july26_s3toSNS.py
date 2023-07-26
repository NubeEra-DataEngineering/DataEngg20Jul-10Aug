import json
import boto3
import logging

def lambda_handler(event, context):
    sns_client = boto3.client('sns')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    topic_arn = 'arn:aws:sns:ap-south-1:475184346033:sns-chiah-assign1'
    for record in event['Records']:
        bucketName = record['s3']['bucket']['name']
        objectKey = record['s3']['object']['key']
        eventType = record['eventName']
    
    if eventType.startswith('ObjectCreated'):
        message = f"Created: s3://{bucketName}/{objectKey}"
    elif event_type.startswith('ObjectRemoved'):
        message = f"Deleted: s3://{bucketName}/{objectKey}"
    else:
        message = f"Unknown: {eventType}"
        
    sns_client.publish(TopicArn=topic_arn, Message=message)
    logger.info(message)
    logger.info('Lambda function executed successfully')
    return 0
