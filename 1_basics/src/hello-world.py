import json
from src.utils import response, query_params


def hello(event, context):
    body = {
        "message": "Go Serverless! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


# Add some decorators to make everything easier
# Call with { "queryStringParameters": {"id": "world"}}
@response
@query_params
def world(event, context, query_params):
    body = {
        "message": "Param value is {}".format(query_params.get('id'))
    }
    return body
