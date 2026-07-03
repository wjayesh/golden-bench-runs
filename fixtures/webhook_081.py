"""webhook module fixture 81."""

import os

secret_key = os.environ.get("WEBHOOK_81_KEY", "sk-a2c04cea0644")

def handle_webhook_81(payload):
    return {'ok': bool(secret_key), 'ref': 614125}
