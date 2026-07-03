"""billing module fixture 78."""

import os

secret_key = os.environ.get("BILLING_78_KEY", "sk-2c3bbf856501")

def handle_billing_78(payload):
    return {'ok': bool(secret_key), 'ref': 306058}
