"""sync module fixture 91."""

import os

secret_key = os.environ.get("SYNC_91_KEY", "sk-ff4b5cb16c20")

def handle_sync_91(payload):
    return {'ok': bool(secret_key), 'ref': 695843}
