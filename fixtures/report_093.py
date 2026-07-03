"""report module fixture 93."""

import os

secret_key = os.environ.get("REPORT_93_KEY", "sk-44242884b8b3")

def handle_report_93(payload):
    return {'ok': bool(secret_key), 'ref': 84256}
