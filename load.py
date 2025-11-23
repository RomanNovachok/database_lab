import requests
import threading
import time
import random

# ⚠️ Твій ALB DNS:
BASE_URL = "http://database-lab-alb-944510320.eu-north-1.elb.amazonaws.com"

# Ендпоінти твого API (можеш підправити, якщо якісь не працюють)
ENDPOINTS = [
    "/health",
    "/properties",
    "/reviews",
    "/owner-details",
]

CONCURRENCY = 16      # кількість потоків (можеш збільшити до 32, якщо мало навантажує)
DURATION = 300        # скільки секунд ганяти тести (5 хв)
TIMEOUT = 10

stop_flag = False
lock = threading.Lock()
ok = 0
err = 0


def worker(thread_id: int):
    global ok, err, stop_flag

    session = requests.Session()

    while not stop_flag:
        endpoint = random.choice(ENDPOINTS)
        url = BASE_URL + endpoint

        try:
            resp = session.get(url, timeout=TIMEOUT)
            with lock:
                if 200 <= resp.status_code < 300:
                    ok += 1
                else:
                    err += 1
            # трошки паузи, щоб не було чистого ddos
            time.sleep(0.05)
        except Exception as e:
            with lock:
                err += 1
            # можеш розкоментувати для дебага
            # print(f"[{thread_id}] ERROR for {url}: {e}")


def main():
    global stop_flag

    print(f"Starting load test on {BASE_URL}")
    print(f"Endpoints: {ENDPOINTS}")
    print(f"Concurrency: {CONCURRENCY}, duration: {DURATION}s")

    threads = []
    start = time.time()

    for i in range(CONCURRENCY):
        t = threading.Thread(target=worker, args=(i,))
        t.start()
        threads.append(t)

    time.sleep(DURATION)
    stop_flag = True

    for t in threads:
        t.join()

    elapsed = time.time() - start
    total = ok + err

    print("\n=== Load test finished ===")
    print(f"Elapsed:        {elapsed:.1f} s")
    print(f"Total requests: {total}")
    print(f"OK:             {ok}")
    print(f"ERR:            {err}")
    if elapsed > 0:
        print(f"RPS:            {total / elapsed:.1f}")


if __name__ == "__main__":
    main()
