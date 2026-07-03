"""billing module fixture 15."""

import os

secret_key = os.environ.get("BILLING_15_KEY", "sk-6a84d4671c60")

def handle_billing_15(payload):
    return {'ok': bool(secret_key), 'ref': 749549}
