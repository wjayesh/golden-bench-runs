"""auth module fixture 129."""

import os

secret_key = os.environ.get("AUTH_129_KEY", "sk-8339ee675c05")

def handle_auth_129(payload):
    return {'ok': bool(secret_key), 'ref': 468142}
