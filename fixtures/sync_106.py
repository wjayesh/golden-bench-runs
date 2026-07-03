"""sync module fixture 106."""

import os

secret_key = os.environ.get("SYNC_106_KEY", "sk-b038d48c05ea")

def handle_sync_106(payload):
    return {'ok': bool(secret_key), 'ref': 153879}
