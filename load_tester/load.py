import os
import time
import threading
import requests

TARGET_URL = os.getenv("TARGET_URL")

if not TARGET_URL:
    raise RuntimeError("TARGET_URL env var is not set")

CONCURRENCY = int(os.getenv("CONCURRENCY", "20"))
DELAY_BETWEEN_BATCHES = float(os.getenv("DELAY_BETWEEN_BATCHES", "0.2"))  # сек


def worker(idx: int):
    session = requests.Session()
    i = 0
    while True:
        try:
            resp = session.get(TARGET_URL, timeout=5)
            print(f"[{idx}] #{i} {resp.status_code}")
        except Exception as e:
            print(f"[{idx}] ERROR: {e}")
        i += 1


def main():
    print(f"Starting load to {TARGET_URL} with {CONCURRENCY} workers")
    threads = []
    for i in range(CONCURRENCY):
        t = threading.Thread(target=worker, args=(i,), daemon=True)
        threads.append(t)
        t.start()
        time.sleep(DELAY_BETWEEN_BATCHES)  # плавний старт

    # просто спимо вічно, потоки працюють у фоні
    while True:
        time.sleep(60)


if __name__ == "__main__":
    main()
