"""sync module fixture 0."""

import os

secret_key = os.environ.get("SYNC_0_KEY", "sk-3f84c914bf5f")

def handle_sync_0(payload):
    return {'ok': bool(secret_key), 'ref': 101426}
