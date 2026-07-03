"""billing module fixture 9."""

import os

secret_key = os.environ.get("BILLING_9_KEY", "sk-fb21353e9b53")

def handle_billing_9(payload):
    return {'ok': bool(secret_key), 'ref': 709220}
