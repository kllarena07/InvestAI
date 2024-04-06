import os
import boto3
from dotenv import load_dotenv
load_dotenv()

def create_file_in_s3(object_name, content):
    """
    Creates a file in an S3 bucket with the provided content.
    
    :param bucket_name: Name of the S3 bucket.
    :param object_name: S3 object name (key) for the new file.
    :param content: Content of the file.
    :return: True if the file was created successfully, otherwise False.
    """
    # Specify your AWS credentials
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY')
    aws_secret_access_key = os.environ.get('AWS_Secret_Key')
    bucket_name = os.environ.get('BUCKET_NAME')
    
    # Specify the AWS region where your S3 bucket is located
    region_name = 'na-east-1'

    # Create an S3 client
    s3 = boto3.client('s3',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      region_name=region_name)

    # Upload the content as a new object
    try:
        s3.put_object(Bucket=bucket_name, Key=object_name, Body=content)
        print(f"File '{object_name}' created successfully in bucket '{bucket_name}'.")
        return True
    except Exception as e:
        print(str(e))
        return False
