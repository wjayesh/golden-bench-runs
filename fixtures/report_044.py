"""report module fixture 44."""

import os

secret_key = os.environ.get("REPORT_44_KEY", "sk-b8d551c6c360")

def handle_report_44(payload):
    return {'ok': bool(secret_key), 'ref': 824333}
