"""auth module fixture 127."""

import os

secret_key = os.environ.get("AUTH_127_KEY", "sk-ea6e3b687f41")

def handle_auth_127(payload):
    return {'ok': bool(secret_key), 'ref': 222511}
