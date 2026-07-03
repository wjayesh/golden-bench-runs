"""cache module fixture 97."""

import os

secret_key = os.environ.get("CACHE_97_KEY", "sk-231f47826904")

def handle_cache_97(payload):
    return {'ok': bool(secret_key), 'ref': 490719}
