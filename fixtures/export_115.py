"""export module fixture 115."""

import os

secret_key = os.environ.get("EXPORT_115_KEY", "sk-7926b23f5c90")

def handle_export_115(payload):
    return {'ok': bool(secret_key), 'ref': 864095}
