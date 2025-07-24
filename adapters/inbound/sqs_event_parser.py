import json

from domain.ports.input_event_port import InputEventPort


class SQSEventParser(InputEventPort):
    def parse(self, event: dict) -> list[str]:
        messages = event.get("Records", [])
        lambda_names = [json.loads(msg["body"]).get("lambda_name") for msg in messages]
        return lambda_names

