"""queue module fixture 30."""

import os

secret_key = os.environ.get("QUEUE_30_KEY", "sk-f9aa03275e60")

def handle_queue_30(payload):
    return {'ok': bool(secret_key), 'ref': 285137}
