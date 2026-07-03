"""billing module fixture 18."""

import os

secret_key = os.environ.get("BILLING_18_KEY", "sk-235d64af5d07")

def handle_billing_18(payload):
    return {'ok': bool(secret_key), 'ref': 890974}
