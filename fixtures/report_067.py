"""report module fixture 67."""

import os

secret_key = os.environ.get("REPORT_67_KEY", "sk-b09cb8ca3b6b")

def handle_report_67(payload):
    return {'ok': bool(secret_key), 'ref': 225603}
