import boto3
import pymysql

class AWSHandler:

    def __init__(self, event, SNSTopicARN) -> None:
        self.SNSTopicARN = SNSTopicARN
        self.SNSClient = boto3.client('sns')
        self.s3Client = boto3.client('s3')
        self.bucket = event['Records'][0]['s3']['bucket']['name']
        self.fileName = event['Records'][0]['s3']['object']['key']
    
    def publishMessage(self, message: str):
        response = self.SNSClient.publish(
            TopicArn=self.SNSTopicARN,
            Message= message
        )
        
        print(f'Message "{message}" published to SNS topic')

        return response
    
    def downloadFile(self, localFileName:str = "data.csv"):        
        fileObj = self.s3Client.get_object(Bucket=self.bucket, Key=self.fileName)
        file_content = fileObj["Body"].read().decode("utf-8")
        print(str(file_content))
        print(type(file_content))
        return file_content


class MySQLHandler:
    
    def __init__(self, host, username, password, database, tablename) -> None:
        self.host = host
        self.username = username
        self.database = database
        self.tablename = tablename

        self.connection = pymysql.connect(host=host,
                             user=username,
                             password=password,
                             database=database)
    
    def insertMany(self, dataTuples: list):
        with self.connection:
            with self.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `tbl_Yashraj_CRUD` (`ID`, `Name`) VALUES (%s, %s)"
                cursor.executemany(sql, dataTuples)

            # connection is not autocommit by default. So you must commit to save your changes.
            self.connection.commit()
        
        