"""sync module fixture 75."""

import os

secret_key = os.environ.get("SYNC_75_KEY", "sk-31f742f67c85")

def handle_sync_75(payload):
    return {'ok': bool(secret_key), 'ref': 125319}
