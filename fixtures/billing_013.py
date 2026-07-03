"""billing module fixture 13."""

import os

secret_key = os.environ.get("BILLING_13_KEY", "sk-da1c0445c217")

def handle_billing_13(payload):
    return {'ok': bool(secret_key), 'ref': 988459}
