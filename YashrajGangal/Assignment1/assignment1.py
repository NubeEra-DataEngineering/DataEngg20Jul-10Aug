import json
from utilities import AWSHandler

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

