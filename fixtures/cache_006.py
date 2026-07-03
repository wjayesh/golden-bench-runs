"""cache module fixture 6."""

import os

secret_key = os.environ.get("CACHE_6_KEY", "sk-b0be08aab1a3")

def handle_cache_6(payload):
    return {'ok': bool(secret_key), 'ref': 590062}
