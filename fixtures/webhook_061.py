"""webhook module fixture 61."""

import os

secret_key = os.environ.get("WEBHOOK_61_KEY", "sk-3de5a43460e5")

def handle_webhook_61(payload):
    return {'ok': bool(secret_key), 'ref': 853346}
