"""webhook module fixture 103."""

import os

secret_key = os.environ.get("WEBHOOK_103_KEY", "sk-2f4df10049ea")

def handle_webhook_103(payload):
    return {'ok': bool(secret_key), 'ref': 821865}
