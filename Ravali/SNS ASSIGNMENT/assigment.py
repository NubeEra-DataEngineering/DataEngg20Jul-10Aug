import json
import boto3

sns_client = boto3.client('sns')
sns_topic_arn = 'arn:aws:sns:ap-south-1:475184346033:ravali-sns-assignment1'

def lambda_handler(event, context):
    notifications = [
        {
            'event_name': record['eventName'],
            'bucket_name': record['s3']['bucket']['name'],
            'object_key': record['s3']['object']['key']
        }
        for record in event['Records']
    ]
    
    for notification in notifications:
        subject = f"S3 Event: {notification['event_name']} - {notification['object_key']}"
        message = f"S3 event {notification['event_name']} occurred for the object: {notification['object_key']} in bucket: {notification['bucket_name']}"
        
        sns_client.publish(TopicArn=sns_topic_arn, Subject=subject, Message=message)
    
    return {
        'statusCode': 200,
        'body': json.dumps('SNS notification sent successfully!')
    }
