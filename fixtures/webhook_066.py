"""webhook module fixture 66."""

import os

secret_key = os.environ.get("WEBHOOK_66_KEY", "sk-9a2062062075")

def handle_webhook_66(payload):
    return {'ok': bool(secret_key), 'ref': 741598}
