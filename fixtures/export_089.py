"""export module fixture 89."""

import os

secret_key = os.environ.get("EXPORT_89_KEY", "sk-7572ec94d363")

def handle_export_89(payload):
    return {'ok': bool(secret_key), 'ref': 187371}
