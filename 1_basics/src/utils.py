import json
import logging
import traceback
import os
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def response(fn):
    def wrapper(*args, **kwargs):
        logger.info("event: {}".format(args[0]))
        try:
            results = fn(*args, **kwargs)
            logger.info("results: {}".format(results))
            return success(results)
        except ValueError as e:
            logger.error("Exception: {}".format(e))
            logger.error("Traceback: {}".format(traceback.format_exc()))
            return error(e, 400)
        except UnauthorizedException as e:
            logger.error("Exception: {}".format(e))
            logger.error("Traceback: {}".format(traceback.format_exc()))
            return error(e, 401)
        except Exception as e:
            logger.error("Exception: {}".format(e))
            logger.error("Traceback: {}".format(traceback.format_exc()))
            return error(e)
    return wrapper


def body(fn):
    def wrapper(*args, **kwargs):

        body = json.loads(args[0]['body'])
        if(body is None):
            raise Exception("A valid Account Body must be passed")
        kwargs.setdefault('body', body)
        results = fn(*args, **kwargs)
        return results
    return wrapper

def path_params(fn):
    def wrapper(*args, **kwargs):

        body = args[0]['pathParameters']
        kwargs.setdefault('path_params', body)
        results = fn(*args, **kwargs)
        return results
    return wrapper

def query_params(fn):
    def wrapper(*args, **kwargs):

        body = args[0]['queryStringParameters']
        kwargs.setdefault('query_params', body)
        results = fn(*args, **kwargs)
        return results
    return wrapper

def success(body, statusCode=200):
    response = {
        "headers": {
            "Access-Control-Allow-Origin": os.environ['cors']
        },
        "statusCode": statusCode,
        "body": json.dumps(body)
    }

    logger.info(response)
    return response


def error(message, statusCode=400):
    response = {
        "headers": {
            "Access-Control-Allow-Origin": os.environ['cors']
        },
        "statusCode": statusCode,
        "body": message
    }
    
    logger.info(response)
    return response

class UnauthorizedException(Exception):
    pass