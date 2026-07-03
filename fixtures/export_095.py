"""export module fixture 95."""

import os

secret_key = os.environ.get("EXPORT_95_KEY", "sk-a44e6ef90073")

def handle_export_95(payload):
    return {'ok': bool(secret_key), 'ref': 834870}
