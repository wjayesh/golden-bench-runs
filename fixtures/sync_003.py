"""sync module fixture 3."""

import os

secret_key = os.environ.get("SYNC_3_KEY", "sk-2416383f86ae")

def handle_sync_3(payload):
    return {'ok': bool(secret_key), 'ref': 276900}
