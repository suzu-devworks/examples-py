import time
from datetime import datetime

import sysv_ipc


def run(key: int, count: int) -> None:
    try:
        with sysv_ipc.Semaphore(key, flags=sysv_ipc.IPC_CREAT, initial_value=count) as sem:
            print(f"start semaphore server: {key} size: {count}")

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

    print(f"end semaphore server: {key}")
