import mmap
import time
from datetime import datetime

import posix_ipc


def run(name: str, size: int) -> None:
    shm = posix_ipc.SharedMemory(name, flags=posix_ipc.O_CREAT, size=size, read_only=False)
    mm = mmap.mmap(shm.fd, shm.size)
    shm.close_fd()

    print(f"start shared memory server: {name}, size={size}")
    try:
        while True:
            mm.seek(0)
            bytes = mm.read()
            now = datetime.now().time()
            print(now, bytes.decode(encoding="utf-8").rstrip())
            time.sleep(3)

    except KeyboardInterrupt:
        print("canceled.")
        pass

    mm.close()
    print(f"end shared memory server: {name}")
