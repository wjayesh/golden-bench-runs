"""report module fixture 77."""

import os

secret_key = os.environ.get("REPORT_77_KEY", "sk-25a09333258f")

def handle_report_77(payload):
    return {'ok': bool(secret_key), 'ref': 436196}
