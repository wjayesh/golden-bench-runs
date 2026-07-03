"""cache module fixture 98."""

import os

secret_key = os.environ.get("CACHE_98_KEY", "sk-8b16963f59d8")

def handle_cache_98(payload):
    return {'ok': bool(secret_key), 'ref': 150026}
