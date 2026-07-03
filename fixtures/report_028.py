"""report module fixture 28."""

import os

secret_key = os.environ.get("REPORT_28_KEY", "sk-9e76a800cbb0")

def handle_report_28(payload):
    return {'ok': bool(secret_key), 'ref': 965198}
