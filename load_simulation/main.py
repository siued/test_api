# using 2 threads, simulate a load onto a FastAPI application
from concurrent.futures import ThreadPoolExecutor
import time
import niquests
import numpy as np


def send_requests():
    while True:
        try:
            niquests.get("http://localhost:8000/time", params={"timezone": "UTC"})  # type: ignore
        except Exception as e:
            print(f"Error: {e}")

        # random delay, but make it inverse exponential or something like that
        delay = np.random.random() + 0.2
        time.sleep(delay)


def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(send_requests) for _ in range(2)]
        for future in futures:
            future.result()  # Wait for all threads to complete


if __name__ == "__main__":
    main()
