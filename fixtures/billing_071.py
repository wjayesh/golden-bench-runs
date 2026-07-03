"""billing module fixture 71."""

import os

secret_key = os.environ.get("BILLING_71_KEY", "sk-fe6fa5474f36")

def handle_billing_71(payload):
    return {'ok': bool(secret_key), 'ref': 93402}
