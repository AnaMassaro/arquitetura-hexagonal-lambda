import json

from adapters.inbound.api_event_parser import APIEventParser
from adapters.inbound.sqs_event_parser import SQSEventParser
from adapters.outbound.boto3_lambda_fetcher import Boto3LambdaFetcher
from application.validate_lambda_config import validate_config


def lambda_handler(event, context):
    if "Records" in event:
        # Evento do SQS
        parser = SQSEventParser()
    else:
        # Evento do API Gateway
        parser = APIEventParser()

    lambda_names = parser.parse(event)
    fetcher = Boto3LambdaFetcher()
    result = validate_config(lambda_names, fetcher)
    return {"statusCode": 200, "body": result}


if __name__ == "__main__":
    # Testando com um evento de exemplo
    test_event = {"Records": [{"body": json.dumps({"lambda_name": "my_lambda_function"})}]}
    print(lambda_handler(test_event, None))

    test_api_event = {"body": json.dumps({"lambda_names": ["my_lambda_function", "another_lambda"]})}
    print(lambda_handler(test_api_event, None))
