import csv
import json
from utilities import AWSHandler, MySQLHandler

topic_arn = 'arn:aws:sns:ap-south-1:475184346033:yashraj-assignment1-bucketActionReport'
DB_HOST = 'db-group-assignment2.ci9rghwaiseb.ap-south-1.rds.amazonaws.com'
DB_USERNAME = 'admin'
DB_PASSWORD = 'admin123'
DB_DATABASE = 'asignement2DB'
DB_TABLE = 'tbl_Yashraj_CRUD'

def lambda_handler(event, context):
    
    # Get file details
    AWSHelper = AWSHandler(event, topic_arn)
    
    # Fetch file from bucket
    CSVFileContent = AWSHelper.downloadFile()
    # with open('data.csv', 'r') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=',')
    #     LOLData = list(reader)
    #     LOTData = [tuple(row) for row in LOLData]
    
    # List of Strings
    # TODO switch to pandas
    LOSData = CSVFileContent.split('\n')
    LOSData = [s.strip() for s in LOSData]
    LOTData = [ tuple(row.split(', ')) for row in LOSData]
    
    # Open MySQL
    MySQLHelper = MySQLHandler(
        host=DB_HOST,
        username=DB_USERNAME,
        password=DB_PASSWORD,
        database=DB_DATABASE,
        tablename=DB_TABLE
        )

    # Load Data into MySQL
    MySQLHelper.insertMany(LOTData)
    
    # Publish reports to SNS
    try:
        SNSClientResponse = AWSHelper.publishMessage(f'{len(LOTData)} rows updated from file {AWSHelper.fileName}')
        return {
            'statusCode': 200,
            'body': json.dumps(SNSClientResponse)
        }
    except Exception as e:
        print('Failed to publish message to SNS topic')
        return {'status': 'error', 'message': str(e)}

