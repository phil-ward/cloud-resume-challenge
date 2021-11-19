let response;
const { DynamoDBClient, UpdateItemCommand } = require("@aws-sdk/client-dynamodb");

/**
 *
 * Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
 * @param {Object} event - API Gateway Lambda Proxy Input Format
 *
 * Context doc: https://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-context.html 
 * @param {Object} context
 *
 * Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
 * @returns {Object} object - API Gateway Lambda Proxy Output Format
 * 
 */
exports.lambdaHandler = async (event, context) => {
    const client = new DynamoDBClient({ region: "us-east-1" });
    const command = new UpdateItemCommand({
        Key: { "ID" : {
                "S" : "visitors"
            }},
        TableName: "cloud-resume-challenge",
        UpdateExpression:  "ADD visitors :inc",
        ExpressionAttributeValues:  {
            ":inc" : {
                N: "1"
            },
        },
    });
    try {
        // const ret = await axios(url);
        const results = await client.send(command);
        response = {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin":  "*",
                "Access-Control-Allow-Methods": "*",
                "Access-Control-Allow-Headers": "*",
            },
                // location: ret.data.trim()
        }
    } catch (err) {
        console.log(err);
        return err;
    }

    return response
};
