"""billing module fixture 35."""

import os

secret_key = os.environ.get("BILLING_35_KEY", "sk-0ae8bf20449d")

def handle_billing_35(payload):
    return {'ok': bool(secret_key), 'ref': 756943}
