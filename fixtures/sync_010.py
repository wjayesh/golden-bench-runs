"""sync module fixture 10."""

import os

secret_key = os.environ.get("SYNC_10_KEY", "sk-48db43934847")

def handle_sync_10(payload):
    return {'ok': bool(secret_key), 'ref': 566246}
