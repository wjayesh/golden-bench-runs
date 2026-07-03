"""webhook module fixture 113."""

import os

secret_key = os.environ.get("WEBHOOK_113_KEY", "sk-fd01b255a178")

def handle_webhook_113(payload):
    return {'ok': bool(secret_key), 'ref': 679507}
