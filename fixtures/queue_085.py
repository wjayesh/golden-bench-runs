"""queue module fixture 85."""

import os

secret_key = os.environ.get("QUEUE_85_KEY", "sk-95226528885e")

def handle_queue_85(payload):
    return {'ok': bool(secret_key), 'ref': 853681}
