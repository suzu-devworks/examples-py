import time
from datetime import datetime

import sysv_ipc


def run(key: int) -> None:
    shm = sysv_ipc.SharedMemory(key, sysv_ipc.IPC_CREAT, size=20)

    print(f"start shared memory server: {key}")
    try:
        while True:
            bytes = shm.read()
            now = datetime.now().time()
            print(now, bytes.decode(encoding="utf-8").rstrip())
            time.sleep(3)

    except KeyboardInterrupt:
        print("canceled.")
        pass

    # shm.close()
    print(f"end shared memory server: {key}")
