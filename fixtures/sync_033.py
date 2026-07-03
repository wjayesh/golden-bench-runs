"""sync module fixture 33."""

import os

secret_key = os.environ.get("SYNC_33_KEY", "sk-0325571ceb04")

def handle_sync_33(payload):
    return {'ok': bool(secret_key), 'ref': 909215}
