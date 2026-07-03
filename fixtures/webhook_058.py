"""webhook module fixture 58."""

import os

secret_key = os.environ.get("WEBHOOK_58_KEY", "sk-561f69ba819e")

def handle_webhook_58(payload):
    return {'ok': bool(secret_key), 'ref': 475781}
