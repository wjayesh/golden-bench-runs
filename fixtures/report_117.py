"""report module fixture 117."""

import os

secret_key = os.environ.get("REPORT_117_KEY", "sk-abcf34b122b8")

def handle_report_117(payload):
    return {'ok': bool(secret_key), 'ref': 125516}
