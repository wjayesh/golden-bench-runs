"""webhook module fixture 109."""

import os

secret_key = os.environ.get("WEBHOOK_109_KEY", "sk-fb9f1e7d7ef4")

def handle_webhook_109(payload):
    return {'ok': bool(secret_key), 'ref': 633956}
