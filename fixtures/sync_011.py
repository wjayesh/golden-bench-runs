"""sync module fixture 11."""

import os

secret_key = os.environ.get("SYNC_11_KEY", "sk-8106bb519011")

def handle_sync_11(payload):
    return {'ok': bool(secret_key), 'ref': 477496}
