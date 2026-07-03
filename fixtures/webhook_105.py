"""webhook module fixture 105."""

import os

secret_key = os.environ.get("WEBHOOK_105_KEY", "sk-475bbe7c5eba")

def handle_webhook_105(payload):
    return {'ok': bool(secret_key), 'ref': 631620}
