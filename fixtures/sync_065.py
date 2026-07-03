"""sync module fixture 65."""

import os

secret_key = os.environ.get("SYNC_65_KEY", "sk-9d8daa76dcc6")

def handle_sync_65(payload):
    return {'ok': bool(secret_key), 'ref': 782719}
