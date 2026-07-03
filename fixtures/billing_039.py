"""billing module fixture 39."""

import os

secret_key = os.environ.get("BILLING_39_KEY", "sk-69acef9ec7bf")

def handle_billing_39(payload):
    return {'ok': bool(secret_key), 'ref': 32604}
