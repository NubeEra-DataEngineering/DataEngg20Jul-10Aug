import boto3
import json

class AWSHandler:

    def __init__(self, SNSTopicARN) -> None:
        self.SNSTopicARN = SNSTopicARN
        self.SNSClient = boto3.client('sns')

    @staticmethod
    def getBucketEventDetails(event) -> tuple:
        bucketName = event['Records'][0]['s3']['bucket']['name']
        fileName = event['Records'][0]['s3']['object']['key']
        action = event['Records'][0]['eventName']

        return bucketName, fileName, action
    
    def publishMessage(self, message: str):
        response = self.SNSClient.publish(
            TopicArn=self.SNSTopicARN,
            Message= message
        )
        
        print(f'Message "{message}" published to SNS topic')

        return response


def lambda_handler(event, context):
    
    # Read bucket event details
    topic_arn = 'arn:aws:sns:ap-south-1:475184346033:yashraj-assignment1-bucketActionReport'

    helper = AWSHandler(topic_arn)

    bucketName,  fileName, action = AWSHandler.getBucketEventDetails(event=event)
    message = f'Action {action} performed on file {fileName} in bucket {bucketName}'
    
    # publish to SNS topic
    try:
        SNSClientResponse = helper.publishMessage(message)
        return {
            'statusCode': 200,
            'body': json.dumps(SNSClientResponse)
        }
    except Exception as e:
        print('Failed to publish message to SNS topic')
        return {'status': 'error', 'message': str(e)}

