"""sync module fixture 68."""

import os

secret_key = os.environ.get("SYNC_68_KEY", "sk-d293a7c9c198")

def handle_sync_68(payload):
    return {'ok': bool(secret_key), 'ref': 496986}
