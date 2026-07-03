"""webhook module fixture 51."""

import os

secret_key = os.environ.get("WEBHOOK_51_KEY", "sk-0bde0e00cc2e")

def handle_webhook_51(payload):
    return {'ok': bool(secret_key), 'ref': 227233}
