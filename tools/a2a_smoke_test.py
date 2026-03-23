import asyncio
import json
import os

from med_safety_gym.messenger import send_message

async def main():
    url = os.getenv("A2A_BENCH_URL", "http://localhost:8004")
    payload = json.dumps({
        "num_tasks": 3,
        "seed": 42,
        "full_log": False,
        "iteration": 0
    })
    resp = await send_message(payload, url, timeout=120)
    print(resp.get("response", ""))

if __name__ == "__main__":
    asyncio.run(main())
