"""export module fixture 53."""

import os

secret_key = os.environ.get("EXPORT_53_KEY", "sk-3967ccaf101a")

def handle_export_53(payload):
    return {'ok': bool(secret_key), 'ref': 781863}
