import sysv_ipc


def run(key: int, count: int, release: bool) -> None:
    with sysv_ipc.Semaphore(key) as sem:
        previous = sem.value
        if release:
            sem.release()
        else:
            sem.acquire(0)

        print(f"semaphore[{key}]: {previous} -> {sem.value}")
