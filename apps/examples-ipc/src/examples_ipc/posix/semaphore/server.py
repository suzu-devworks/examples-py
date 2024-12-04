import time
from datetime import datetime

import posix_ipc


def run(name: str, count: int) -> None:
    sem = posix_ipc.Semaphore(name, flags=posix_ipc.O_CREAT, initial_value=count)

    print(f"start semaphore server: {name} size: {count}")
    try:
        previous = None
        while True:
            if previous != sem.value:
                previous = sem.value
                now = datetime.now().time()
                print(now, f"semaphore: {sem.value}")

            time.sleep(1)

    except KeyboardInterrupt:
        print("canceled.")
        pass

    sem.close()
    print(f"end semaphore server: {name}")
