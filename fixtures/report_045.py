"""report module fixture 45."""

import os

secret_key = os.environ.get("REPORT_45_KEY", "sk-67c6417085da")

def handle_report_45(payload):
    return {'ok': bool(secret_key), 'ref': 52674}
