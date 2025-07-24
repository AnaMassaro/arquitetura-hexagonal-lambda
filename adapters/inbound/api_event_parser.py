import json

from domain.ports.input_event_port import InputEventPort


class APIEventParser(InputEventPort):
    def parse(self, event: dict) -> list[str]:
        body = event.get("body")
        if isinstance(body, str):
            body = json.loads(body)
        return body.get("lambda_names", [])

