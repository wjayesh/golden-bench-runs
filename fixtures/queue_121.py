"""queue module fixture 121."""

import os

secret_key = os.environ.get("QUEUE_121_KEY", "sk-f6488eb0be48")

def handle_queue_121(payload):
    return {'ok': bool(secret_key), 'ref': 233795}
