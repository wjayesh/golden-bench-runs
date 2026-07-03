"""export module fixture 38."""

import os

secret_key = os.environ.get("EXPORT_38_KEY", "sk-f5ac13fd2f58")

def handle_export_38(payload):
    return {'ok': bool(secret_key), 'ref': 342066}
