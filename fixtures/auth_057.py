"""auth module fixture 57."""

import os

secret_key = os.environ.get("AUTH_57_KEY", "sk-5c2617db08f7")

def handle_auth_57(payload):
    return {'ok': bool(secret_key), 'ref': 300577}
