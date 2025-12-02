import os
import time
import random
import string
import threading

import requests

# 🔴 Твій ALB, як і було раніше
BASE_URL = os.getenv(
    "API_URL",
    "http://database-lab-alb-944510320.eu-north-1.elb.amazonaws.com",
)

# Скільки потоків генерують навантаження
NUM_WORKERS = int(os.getenv("WORKERS", "10"))

# Пауза між циклами кожного воркера (секунди)
SLEEP_BETWEEN_LOOPS = float(os.getenv("SLEEP", "0.05"))


def random_string(length: int = 10) -> str:
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def worker(worker_id: int) -> None:
    print(f"[worker {worker_id}] started")
    while True:
        try:
            # кілька INSERT підряд
            for _ in range(5):
                item = random_string()
                r = requests.post(
                    BASE_URL + "/insert",
                    json={"item": item},
                    timeout=3,
                )
                print(f"[worker {worker_id}] INSERT {r.status_code}")

            # один GET items
            r = requests.get(BASE_URL + "/items", timeout=3)
            print(f"[worker {worker_id}] GET /items {r.status_code}")

        except Exception as e:
            print(f"[worker {worker_id}] ERROR: {e}")

        time.sleep(SLEEP_BETWEEN_LOOPS)


def main():
    print(
        f"Load tester starting against {BASE_URL}, "
        f"workers={NUM_WORKERS}, sleep={SLEEP_BETWEEN_LOOPS}"
    )

    threads = []
    for i in range(NUM_WORKERS):
        t = threading.Thread(target=worker, args=(i,), daemon=True)
        t.start()
        threads.append(t)

    # просто тримаємо процес живим
    while True:
        time.sleep(10)


if __name__ == "__main__":
    main()
