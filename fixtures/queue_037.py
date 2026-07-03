"""queue module fixture 37."""

import os

secret_key = os.environ.get("QUEUE_37_KEY", "sk-ba125efa32f1")

def handle_queue_37(payload):
    return {'ok': bool(secret_key), 'ref': 176029}
