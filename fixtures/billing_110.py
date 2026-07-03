"""billing module fixture 110."""

import os

secret_key = os.environ.get("BILLING_110_KEY", "sk-72de9ef8838d")

def handle_billing_110(payload):
    return {'ok': bool(secret_key), 'ref': 442933}
