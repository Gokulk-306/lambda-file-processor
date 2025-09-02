import json
import boto3
import time

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FileMetadata')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        size = record['s3']['object']['size']
        
        table.put_item(
            Item={
                'FileName': key,
                'Size': size,
                'UploadTime': int(time.time())
            }
        )
        
        print(f"Processed file: {key}, size: {size}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('File processed successfully!')
    }
