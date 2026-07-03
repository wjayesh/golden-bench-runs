"""webhook module fixture 48."""

import os

secret_key = os.environ.get("WEBHOOK_48_KEY", "sk-ba4521dac634")

def handle_webhook_48(payload):
    return {'ok': bool(secret_key), 'ref': 808811}
