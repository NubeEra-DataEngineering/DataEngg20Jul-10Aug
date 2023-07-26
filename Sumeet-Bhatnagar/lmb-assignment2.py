import json
import boto3
import pandas as pd
from sqlalchemy import create_engine


aws_region_name = "ap-south-1"
s3_client = boto3.client("s3", region_name=aws_region_name)
sns_client = boto3.client("sns", region_name=aws_region_name)
rds_username = "admin"
rds_password = "admin123"
rds_endpoint = "db-group-assignment2.ci9rghwaiseb.ap-south-1.rds.amazonaws.com"
db_name = "asignement2DB"
rds_engine_url = (
    f"mysql+mysqlconnector://{rds_username}:{rds_password}@{rds_endpoint}:3306/{db_name}"
)


def lambda_handler(event, context):
    # TODO implement
    print("Starting up")
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    key_name = event["Records"][0]["s3"]["object"]["key"]

    print(event)

    print(bucket_name, key_name)

    key_name_ext = key_name.split(".")[-1].lower()

    table_name = "tbl_sumeet_crud"

    if key_name_ext == "csv":
        print("file extension matches")

        obj = s3_client.get_object(Bucket=bucket_name, Key=key_name)

        df = pd.read_csv(obj["Body"])
        print(df.head())
        try:
            rds_engine = create_engine(rds_engine_url)
        except Exception as e:
            print(e)
            print("connection to rds failed")
            return {"statusCode": 200, "body": json.dumps("Connetion to rds failed")}

        try:
            df.to_sql(
                table_name,  # Name of SQL table.
                rds_engine,  # sqlalchemy.engine.Engine or sqlite3.Connection
                if_exists="append",  # How to behave if the table already exists. You can use 'replace', 'append' to replace it.
                index=False,  # It means index of DataFrame will save. Set False to ignore the index of DataFrame.
            )
        except Exception as e:
            print(e)
            print("addition to rds tables failed")
            return {
                "statusCode": 200,
                "body": json.dumps("Addition to rds tables failed"),
            }

        row_inserted = len(df)
        message_body = f"s3:\\{bucket_name}\\{key_name}\nCount: {row_inserted} Inserted"

        print(message_body)        

        sns_client.publish(
            TopicArn="arn:aws:sns:ap-south-1:475184346033:tp-sumeetb-assignment1",
            Message=message_body,
        )

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}


if __name__ == "__main__":
    event = {
        "Records": [
            {
                "eventVersion": "2.1",
                "eventSource": "aws:s3",
                "awsRegion": "ap-south-1",
                "eventTime": "2023-07-26T21:34:04.712Z",
                "eventName": "ObjectCreated:Put",
                "userIdentity": {"principalId": "AWS:AIDAW5IZRWOY5QFBDR2U6"},
                "requestParameters": {"sourceIPAddress": "72.68.49.193"},
                "responseElements": {
                    "x-amz-request-id": "ZZQE5AE3A1S6GWBA",
                    "x-amz-id-2": "NBreJ4W079bKsDtp4/1I2LxzN5gTfFOLzp3K8JAi0JFkCIRCt/rSzLFHbO0X00bCYDKveSDf26CjvAHdWhzrrukJpGNdiskZ",
                },
                "s3": {
                    "s3SchemaVersion": "1.0",
                    "configurationId": "0759e3d0-f60c-4b77-90ff-df6f20f26fd8",
                    "bucket": {
                        "name": "bkt-sumeetb-assignment2",
                        "ownerIdentity": {"principalId": "ATNOUIIGG5RVQ"},
                        "arn": "arn:aws:s3:::bkt-sumeetb-assignment2",
                    },
                    "object": {
                        "key": "sample_data.csv",
                        "size": 134,
                        "eTag": "4669856eb17422178dc1776cd471169e",
                        "sequencer": "0064C1914CAC717918",
                    },
                },
            }
        ]
    }

    context = {}
    lambda_handler(event, context)
    pass
