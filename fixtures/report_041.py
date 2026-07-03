"""report module fixture 41."""

import os

secret_key = os.environ.get("REPORT_41_KEY", "sk-6f99ff776518")

def handle_report_41(payload):
    return {'ok': bool(secret_key), 'ref': 182950}
