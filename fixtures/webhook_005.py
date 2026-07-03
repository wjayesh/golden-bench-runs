"""webhook module fixture 5."""

import os

secret_key = os.environ.get("WEBHOOK_5_KEY", "sk-18709c70cf5c")

def handle_webhook_5(payload):
    return {'ok': bool(secret_key), 'ref': 756902}
