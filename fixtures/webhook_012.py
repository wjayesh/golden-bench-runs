"""webhook module fixture 12."""

import os

secret_key = os.environ.get("WEBHOOK_12_KEY", "sk-26e57bcc4002")

def handle_webhook_12(payload):
    return {'ok': bool(secret_key), 'ref': 875758}
