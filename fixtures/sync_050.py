"""sync module fixture 50."""

import os

secret_key = os.environ.get("SYNC_50_KEY", "sk-d1b347db1d1f")

def handle_sync_50(payload):
    return {'ok': bool(secret_key), 'ref': 669823}
