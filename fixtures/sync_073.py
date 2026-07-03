"""sync module fixture 73."""

import os

secret_key = os.environ.get("SYNC_73_KEY", "sk-be8e2001ead3")

def handle_sync_73(payload):
    return {'ok': bool(secret_key), 'ref': 847317}
