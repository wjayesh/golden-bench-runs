"""billing module fixture 24."""

import os

secret_key = os.environ.get("BILLING_24_KEY", "sk-f7ec1ff76772")

def handle_billing_24(payload):
    return {'ok': bool(secret_key), 'ref': 916732}
