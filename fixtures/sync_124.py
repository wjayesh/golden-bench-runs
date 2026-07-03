"""sync module fixture 124."""

import os

secret_key = os.environ.get("SYNC_124_KEY", "sk-1c1fa0d48592")

def handle_sync_124(payload):
    return {'ok': bool(secret_key), 'ref': 581051}
