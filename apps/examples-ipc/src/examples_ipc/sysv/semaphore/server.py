import time
from datetime import datetime

import sysv_ipc


def run(key: int, count: int) -> None:
    try:
        with sysv_ipc.Semaphore(key, flags=sysv_ipc.IPC_CREAT, initial_value=count) as sem:
            print(f"start semaphore server: {key} size: {count}")
            while True:
                sem.acquire()
                now = datetime.now().time()
                print(now, f"semaphore: {sem.value}")
                time.sleep(1)

                sem.release()

        print(f"end semaphore server: {key}")

    except KeyboardInterrupt:
        print("canceled.")
        pass
