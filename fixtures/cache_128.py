"""cache module fixture 128."""

import os

secret_key = os.environ.get("CACHE_128_KEY", "sk-1a05e97d0655")

def handle_cache_128(payload):
    return {'ok': bool(secret_key), 'ref': 550785}
