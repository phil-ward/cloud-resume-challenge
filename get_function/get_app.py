import json
import boto3


def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cloud-resume-challenge')

    get_response = table.get_item(
        Key={
            "ID": "visitors"
        }
    )
    current_count = get_response['Item']

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*",
        },
        "body": json.dumps({
            "count": f'{current_count["total_visitors"]}',
        }),
    }
