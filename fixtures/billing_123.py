"""billing module fixture 123."""

import os

secret_key = os.environ.get("BILLING_123_KEY", "sk-8f19aa7a97c1")

def handle_billing_123(payload):
    return {'ok': bool(secret_key), 'ref': 243964}
