"""billing module fixture 27."""

import os

secret_key = os.environ.get("BILLING_27_KEY", "sk-bac0d6c4833f")

def handle_billing_27(payload):
    return {'ok': bool(secret_key), 'ref': 253578}
