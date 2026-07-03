"""sync module fixture 14."""

import os

secret_key = os.environ.get("SYNC_14_KEY", "sk-ab24d3e24a25")

def handle_sync_14(payload):
    return {'ok': bool(secret_key), 'ref': 871284}
