"""billing module fixture 74."""

import os

secret_key = os.environ.get("BILLING_74_KEY", "sk-e8109d4cb127")

def handle_billing_74(payload):
    return {'ok': bool(secret_key), 'ref': 970561}
