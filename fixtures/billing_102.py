"""billing module fixture 102."""

import os

secret_key = os.environ.get("BILLING_102_KEY", "sk-c402a75f2a0c")

def handle_billing_102(payload):
    return {'ok': bool(secret_key), 'ref': 577219}
