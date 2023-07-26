import json
import boto3
import os
import logging

aws_region_name = os.environ.get('AWS_REGION','ap-south-1')

sns_client = boto3.client("sns",region_name=aws_region_name)
s3_client = boto3.client("s3",region_name=aws_region_name)

logger = logging.getLogger()

logger.setLevel('INFO')


def lambda_handler(event, context):
    # TODO implement

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    event_name = event['Records'][0]['eventName']
    
    message = f'{event_name} event occured for {key} object in {bucket} bucket'
    
    logger.info(message)
    
    sns_client.publish(
        TopicArn='arn:aws:sns:ap-south-1:475184346033:tp-sumeetb-assignment1',
        Message=message
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
