"""auth module fixture 64."""

import os

secret_key = os.environ.get("AUTH_64_KEY", "sk-c14d3de2c34b")

def handle_auth_64(payload):
    return {'ok': bool(secret_key), 'ref': 728989}
