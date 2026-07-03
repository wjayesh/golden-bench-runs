"""export module fixture 80."""

import os

secret_key = os.environ.get("EXPORT_80_KEY", "sk-b289b6a50a5c")

def handle_export_80(payload):
    return {'ok': bool(secret_key), 'ref': 662771}
