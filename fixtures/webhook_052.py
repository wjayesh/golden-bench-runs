"""webhook module fixture 52."""

import os

secret_key = os.environ.get("WEBHOOK_52_KEY", "sk-9e51588f475a")

def handle_webhook_52(payload):
    return {'ok': bool(secret_key), 'ref': 404872}
