"""sync module fixture 92."""

import os

secret_key = os.environ.get("SYNC_92_KEY", "sk-2b65c416a376")

def handle_sync_92(payload):
    return {'ok': bool(secret_key), 'ref': 532832}
