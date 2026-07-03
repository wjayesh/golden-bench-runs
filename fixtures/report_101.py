"""report module fixture 101."""

import os

secret_key = os.environ.get("REPORT_101_KEY", "sk-00ec35c03c86")

def handle_report_101(payload):
    return {'ok': bool(secret_key), 'ref': 828390}
