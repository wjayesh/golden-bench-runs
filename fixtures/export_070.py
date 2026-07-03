"""export module fixture 70."""

import os

secret_key = os.environ.get("EXPORT_70_KEY", "sk-cb4f76e011a3")

def handle_export_70(payload):
    return {'ok': bool(secret_key), 'ref': 732290}
