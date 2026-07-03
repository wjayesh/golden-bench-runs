"""sync module fixture 29."""

import os

secret_key = os.environ.get("SYNC_29_KEY", "sk-1ecfff9866e8")

def handle_sync_29(payload):
    return {'ok': bool(secret_key), 'ref': 851159}
