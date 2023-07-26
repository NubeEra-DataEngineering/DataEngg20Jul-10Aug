import boto3

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
