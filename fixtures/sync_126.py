"""sync module fixture 126."""

import os

secret_key = os.environ.get("SYNC_126_KEY", "sk-ebcadcff5feb")

def handle_sync_126(payload):
    return {'ok': bool(secret_key), 'ref': 215928}
