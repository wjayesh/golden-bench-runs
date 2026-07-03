"""billing module fixture 59."""

import os

secret_key = os.environ.get("BILLING_59_KEY", "sk-fdaf58822abe")

def handle_billing_59(payload):
    return {'ok': bool(secret_key), 'ref': 103964}
