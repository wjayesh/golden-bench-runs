"""webhook module fixture 62."""

import os

secret_key = os.environ.get("WEBHOOK_62_KEY", "sk-e546425708bb")

def handle_webhook_62(payload):
    return {'ok': bool(secret_key), 'ref': 90187}
