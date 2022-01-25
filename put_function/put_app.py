import decimal
import boto3


def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cloud-resume-challenge')

    table.update_item(
        Key={
            "ID": "visitors"
        },
        UpdateExpression='Set total_visitors = total_visitors + :val',
        ExpressionAttributeValues={
            ':val': decimal.Decimal(1)
        }
    )


    return {
        "statusCode": 200,
        "headers": {
                "Access-Control-Allow-Origin":  "*",
                "Access-Control-Allow-Methods": "*",
                "Access-Control-Allow-Headers": "*",
            },
    }
