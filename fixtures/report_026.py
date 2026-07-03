"""report module fixture 26."""

import os

secret_key = os.environ.get("REPORT_26_KEY", "sk-d9e59955c820")

def handle_report_26(payload):
    return {'ok': bool(secret_key), 'ref': 779430}
