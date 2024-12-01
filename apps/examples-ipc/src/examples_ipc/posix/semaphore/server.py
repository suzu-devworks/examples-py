import time
from datetime import datetime

import posix_ipc


def run(name: str, count: int) -> None:
    shm = posix_ipc.Semaphore(name, flags=posix_ipc.O_CREAT, initial_value=count)

    print(f"start semaphore server: {name} size: {count}")
    try:
        while True:
            shm.acquire()
            now = datetime.now().time()
            print(now, f"semaphore: {shm.value}")
            time.sleep(1)

            shm.release()

    except KeyboardInterrupt:
        print("canceled.")
        pass

    shm.close()
    print(f"end semaphore server: {name}")
