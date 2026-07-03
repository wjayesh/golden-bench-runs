"""export module fixture 122."""

import os

secret_key = os.environ.get("EXPORT_122_KEY", "sk-07367aaa7db9")

def handle_export_122(payload):
    return {'ok': bool(secret_key), 'ref': 929205}
