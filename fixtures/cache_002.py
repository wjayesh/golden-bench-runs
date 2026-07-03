"""cache module fixture 2."""

import os

secret_key = os.environ.get("CACHE_2_KEY", "sk-9b62305ea303")

def handle_cache_2(payload):
    return {'ok': bool(secret_key), 'ref': 187463}
