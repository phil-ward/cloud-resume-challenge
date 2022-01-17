import decimal
import json
import boto3


# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cloud-resume-challenge')

    get_response = table.get_item(
        Key={
            "ID": "visitors"
        }
    )
    current_count = get_response['Item']

    put_response = table.update_item(
        Key={
            "ID": "visitors"
        },
        UpdateExpression='Set visitors = visitors + :val',
        ExpressionAttributeValues={
            ':val': decimal.Decimal(1)
        }
    )
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "headers": {
                "Access-Control-Allow-Origin":  "*",
                "Access-Control-Allow-Methods": "*",
                "Access-Control-Allow-Headers": "*",
            },
    }
