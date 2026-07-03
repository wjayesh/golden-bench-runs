"""webhook module fixture 100."""

import os

secret_key = os.environ.get("WEBHOOK_100_KEY", "sk-1b9367b80184")

def handle_webhook_100(payload):
    return {'ok': bool(secret_key), 'ref': 127045}
