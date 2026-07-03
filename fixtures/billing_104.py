"""billing module fixture 104."""

import os

secret_key = os.environ.get("BILLING_104_KEY", "sk-1c75baba1b8d")

def handle_billing_104(payload):
    return {'ok': bool(secret_key), 'ref': 116246}
