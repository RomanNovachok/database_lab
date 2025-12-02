import requests
import time
import threading
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "http://database-lab-alb-944510320.eu-north-1.elb.amazonaws.com"

# скільки паралельних “воркерів” будемо ганяти
WORKERS = 20

def spam_health():
    while True:
        try:
            resp = requests.get(BASE_URL + "/health", timeout=3)
            print("Health:", resp.status_code)
        except Exception as e:
            print("ERROR /health:", e)
        # мінімальна пауза, щоб не вбити сам load-tester
        time.sleep(0.01)

def spam_read():
    while True:
        try:
            resp = requests.get(BASE_URL + "/read?key=test", timeout=3)
            print("READ:", resp.status_code)
        except Exception as e:
            print("ERROR /read:", e)
        time.sleep(0.01)

def spam_write():
    while True:
        try:
            resp = requests.post(
                BASE_URL + "/write",
                json={"key": "test", "value": "x" * 1000},
                timeout=3,
            )
            print("WRITE:", resp.status_code)
        except Exception as e:
            print("ERROR /write:", e)
        time.sleep(0.01)

def worker_loop(worker_id: int):
    # кожен воркер по колу робить health/read/write
    while True:
        spam_health()
        spam_read()
        spam_write()

def main():
    print(f"Start heavy load to {BASE_URL} with {WORKERS} workers")

    # окремий пул потоків
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        for i in range(WORKERS):
            executor.submit(worker_loop, i)

        # ніколи не виходимо
        while True:
            time.sleep(10)

if __name__ == "__main__":
    main()
