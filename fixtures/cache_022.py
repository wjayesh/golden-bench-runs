"""cache module fixture 22."""

import os

secret_key = os.environ.get("CACHE_22_KEY", "sk-849147d1b548")

def handle_cache_22(payload):
    return {'ok': bool(secret_key), 'ref': 602589}
