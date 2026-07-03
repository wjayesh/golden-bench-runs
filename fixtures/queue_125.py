"""queue module fixture 125."""

import os

secret_key = os.environ.get("QUEUE_125_KEY", "sk-9012b869cc63")

def handle_queue_125(payload):
    return {'ok': bool(secret_key), 'ref': 366163}
