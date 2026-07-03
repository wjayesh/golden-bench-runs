"""webhook module fixture 55."""

import os

secret_key = os.environ.get("WEBHOOK_55_KEY", "sk-979a86b427a6")

def handle_webhook_55(payload):
    return {'ok': bool(secret_key), 'ref': 627720}
