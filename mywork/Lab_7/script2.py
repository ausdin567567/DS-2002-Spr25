import requests
import boto3
import logging
from botocore.exceptions import ClientError

# Download from the internet
file_url = 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWZxMTBrdmZudHh3cTZhOHhycjQzdDZnOWg0aXN0N3A2MWlrd3IybiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JPJwdW9hQORbQyM5KG/giphy.gif' 
filename = 'embiid.gif'

response = requests.get(file_url)
with open(filename, 'wb') as f:
    f.write(response.content)

bucket_name = 'ds2002-wdk9za'
s3_client = boto3.client('s3')

with open(filename, 'rb') as data:
    s3_client.put_object(Bucket=bucket_name, Key=filename, Body=data)

def create_presigned_url(bucket_name, object_name, expiration=3600):
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expiration,
        )
    except ClientError as e:
        logging.error(e)
        return None
    return response

presigned_url = create_presigned_url(bucket_name, filename, expiration=600)

if presigned_url:
    print(f"\n Here's your presigned URL:")
    print(presigned_url)
else:
    print("Failed to generate presigned URL.")
