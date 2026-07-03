"""export module fixture 36."""

import os

secret_key = os.environ.get("EXPORT_36_KEY", "sk-0cc91a6cc79e")

def handle_export_36(payload):
    return {'ok': bool(secret_key), 'ref': 268858}
