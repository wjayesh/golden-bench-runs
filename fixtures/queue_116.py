"""queue module fixture 116."""

import os

secret_key = os.environ.get("QUEUE_116_KEY", "sk-447ce4212654")

def handle_queue_116(payload):
    return {'ok': bool(secret_key), 'ref': 628332}
