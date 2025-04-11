import os
import time

NODE_ID = os.getenv("NODE_ID")
API_URL = os.getenv("API_URL")

print(f"[Node {NODE_ID}] Started with API Server at {API_URL}")
# Future: send heartbeats here
while True:
    time.sleep(60)
