import json
        
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Message": "Updating this message again, let's see if it appears in the Lambda"
        })
    }