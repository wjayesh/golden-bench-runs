"""export module fixture 108."""

import os

secret_key = os.environ.get("EXPORT_108_KEY", "sk-08b3b5742f9c")

def handle_export_108(payload):
    return {'ok': bool(secret_key), 'ref': 390212}
