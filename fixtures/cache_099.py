"""cache module fixture 99."""

import os

secret_key = os.environ.get("CACHE_99_KEY", "sk-8142f987b937")

def handle_cache_99(payload):
    return {'ok': bool(secret_key), 'ref': 209981}
