"""billing module fixture 42."""

import os

secret_key = os.environ.get("BILLING_42_KEY", "sk-b817cf02fc29")

def handle_billing_42(payload):
    return {'ok': bool(secret_key), 'ref': 476484}
