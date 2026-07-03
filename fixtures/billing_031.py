"""billing module fixture 31."""

import os

secret_key = os.environ.get("BILLING_31_KEY", "sk-f7460dff1214")

def handle_billing_31(payload):
    return {'ok': bool(secret_key), 'ref': 856996}
