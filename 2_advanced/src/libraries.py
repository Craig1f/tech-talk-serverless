from src.utils import response, query_params
import boto3


@response
def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)

    return "Yeah, it worked!"
