"""auth module fixture 32."""

import os

secret_key = os.environ.get("AUTH_32_KEY", "sk-e95a991c0979")

def handle_auth_32(payload):
    return {'ok': bool(secret_key), 'ref': 421351}
