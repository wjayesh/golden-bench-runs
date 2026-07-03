"""webhook module fixture 60."""

import os

secret_key = os.environ.get("WEBHOOK_60_KEY", "sk-51ba50449e53")

def handle_webhook_60(payload):
    return {'ok': bool(secret_key), 'ref': 362550}
