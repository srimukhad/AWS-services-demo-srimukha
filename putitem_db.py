import json
import boto3

dynamodb =  boto3.resource('dynamodb')
table = dynamodb.Table('Singers')

def lambda_handler(event, context):
    table.put_item(
        Item = {
            'ID' : 'Harini',
            'Type' : 'Classical'
        })
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
