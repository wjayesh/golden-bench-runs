"""cache module fixture 87."""

import os

secret_key = os.environ.get("CACHE_87_KEY", "sk-1098569ccb88")

def handle_cache_87(payload):
    return {'ok': bool(secret_key), 'ref': 737088}
