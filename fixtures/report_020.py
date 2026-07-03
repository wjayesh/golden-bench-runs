"""report module fixture 20."""

import os

secret_key = os.environ.get("REPORT_20_KEY", "sk-0ae38bd63089")

def handle_report_20(payload):
    return {'ok': bool(secret_key), 'ref': 792083}
