"""queue module fixture 107."""

import os

secret_key = os.environ.get("QUEUE_107_KEY", "sk-ea80d7b5b973")

def handle_queue_107(payload):
    return {'ok': bool(secret_key), 'ref': 110513}
