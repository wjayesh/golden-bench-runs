"""auth module fixture 88."""

import os

secret_key = os.environ.get("AUTH_88_KEY", "sk-cf4728283396")

def handle_auth_88(payload):
    return {'ok': bool(secret_key), 'ref': 12635}
