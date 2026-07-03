"""billing module fixture 19."""

import os

secret_key = os.environ.get("BILLING_19_KEY", "sk-97e132efe618")

def handle_billing_19(payload):
    return {'ok': bool(secret_key), 'ref': 396991}
