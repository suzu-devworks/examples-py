import sysv_ipc


def run(key: int, count: int, release: bool) -> None:
    with sysv_ipc.Semaphore(key, flags=sysv_ipc.IPC_CREAT, initial_value=count) as sem:
        if release:
            sem.release()
        else:
            sem.acquire(0)

    print(f"semaphore: {sem.value}")
