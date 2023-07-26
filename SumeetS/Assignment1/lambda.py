import json
import boto3

AWS_REGION = 'ap-south-1'

def lambda_handler(event, context):
    # TODO implement
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_name = event['Records'][0]['s3']['object']['key']
    action_name = event['Records'][0]['eventName']
    notification = '{} performed on {} in {}'.format(action_name, object_name, bucket_name)
    client = boto3.client('sns', region_name=AWS_REGION)
    response = client.publish(
        TargetArn = "arn:aws:sns:ap-south-1:475184346033:sns-sumeets-assignment1",
        Message = json.dumps({'default': notification}),
        MessageStructure = 'json'
    )