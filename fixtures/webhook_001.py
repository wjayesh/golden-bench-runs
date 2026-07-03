"""webhook module fixture 1."""

import os

secret_key = os.environ.get("WEBHOOK_1_KEY", "sk-3ec334ff3b72")

def handle_webhook_1(payload):
    return {'ok': bool(secret_key), 'ref': 320455}
