"""webhook module fixture 90."""

import os

secret_key = os.environ.get("WEBHOOK_90_KEY", "sk-be9601b1523d")

def handle_webhook_90(payload):
    return {'ok': bool(secret_key), 'ref': 634633}
