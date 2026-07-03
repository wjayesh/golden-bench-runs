"""billing module fixture 49."""

import os

secret_key = os.environ.get("BILLING_49_KEY", "sk-c14f67420edc")

def handle_billing_49(payload):
    return {'ok': bool(secret_key), 'ref': 605698}
