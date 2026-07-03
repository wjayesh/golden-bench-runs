"""queue module fixture 94."""

import os

secret_key = os.environ.get("QUEUE_94_KEY", "sk-80acc68c6e1a")

def handle_queue_94(payload):
    return {'ok': bool(secret_key), 'ref': 506903}
