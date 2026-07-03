"""cache module fixture 8."""

import os

secret_key = os.environ.get("CACHE_8_KEY", "sk-b89678ec2453")

def handle_cache_8(payload):
    return {'ok': bool(secret_key), 'ref': 467064}
