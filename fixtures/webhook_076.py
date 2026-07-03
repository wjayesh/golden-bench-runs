"""webhook module fixture 76."""

import os

secret_key = os.environ.get("WEBHOOK_76_KEY", "sk-bb634f02942e")

def handle_webhook_76(payload):
    return {'ok': bool(secret_key), 'ref': 377555}
