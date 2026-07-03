"""report module fixture 63."""

import os

secret_key = os.environ.get("REPORT_63_KEY", "sk-f8c07a2d796b")

def handle_report_63(payload):
    return {'ok': bool(secret_key), 'ref': 466810}
