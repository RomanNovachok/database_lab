import requests
import time

BASE_URL = "http://database-lab-alb-944510320.eu-north-1.elb.amazonaws.com"  # 🔴 свій ALB

def main():
    print(f"Start sending load to {BASE_URL}")
    while True:
        try:
            resp = requests.get(BASE_URL + "/health", timeout=5)
            print("Health:", resp.status_code)
        except Exception as e:
            print("ERROR:", e)
        time.sleep(0.2)

if __name__ == "__main__":
    main()
