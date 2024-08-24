import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello, this is your simple AWS Lambda function!'
    }
