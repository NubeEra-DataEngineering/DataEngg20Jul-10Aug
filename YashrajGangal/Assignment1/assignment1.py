import boto3
import json

def lambda_handler(event, context):
    
    # Read bucket event details
    # print(event)
    bucketName = event['Records'][0]['s3']['bucket']['name']
    fileName = event['Records'][0]['s3']['object']['key']
    action = event['Records'][0]['eventName']
    message = f'Action {action} performed on file {fileName} in bucket {bucketName}'
    
    # publish to SNS topic
    sns = boto3.client('sns')
    try:
        # Publish a message to the the Demo_Topic
        topic_arn = 'arn:aws:sns:ap-south-1:475184346033:yashraj-assignment1-bucketActionReport'
        
        response = sns.publish(
            TopicArn=topic_arn,
            Message= message
        )
        
        print(f'Message "{message}" published to SNS topic')
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    except Exception as e:
        print('Failed to publish message to SNS topic')
        return {'status': 'error', 'message': str(e)}

