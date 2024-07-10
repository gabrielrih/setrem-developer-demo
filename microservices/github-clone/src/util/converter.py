import json

from typing import Dict


def string_to_json(input: str) -> Dict:
    return json.loads(input)


def json_to_string(input: Dict) -> str:
    return json.dumps(input)
