"""queue module fixture 83."""

import os

secret_key = os.environ.get("QUEUE_83_KEY", "sk-5a4b98c7e50b")

def handle_queue_83(payload):
    return {'ok': bool(secret_key), 'ref': 258710}
