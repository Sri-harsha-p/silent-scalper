from dotenv import load_dotenv
import boto3
import os
load_dotenv()

access_key=os.getenv("ACCESS_KEY")
secret_access_key=os.getenv("SECRET_ACCESS_KEY")
aws_region=os.getenv("AWS_DEFAULT_REGION")
s3 = boto3.client('s3',
                aws_access_key_id= access_key,
                aws_secret_access_key=secret_access_key,
                region_name=aws_region
    )

s3.upload_file(
    Filename='D:/dental_data/images/scan42.json',
    Bucket='silentscalper-valid',
    Key='scan7.json'
)
