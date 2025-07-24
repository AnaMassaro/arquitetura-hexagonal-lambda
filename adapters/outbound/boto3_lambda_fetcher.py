# import boto3
from domain.ports.lambda_data_port import LambdaDataPort


class Boto3LambdaFetcher(LambdaDataPort):
    def __init__(self):
        self.client = "Mock Client"

    def get_runtime(self, lambda_name: str) -> str:
        response = {"FunctionName": lambda_name, "Runtime": "python3.9"}  # Mocked response for demonstration
        return response.get("Runtime", "unknown")

