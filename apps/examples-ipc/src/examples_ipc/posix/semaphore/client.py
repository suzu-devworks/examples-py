import posix_ipc


def run(name: str, count: int, release: bool) -> None:
    shm = posix_ipc.Semaphore(name, flags=posix_ipc.O_CREAT, initial_value=count)

    if release:
        shm.release()
    else:
        shm.acquire(0)

    print(f"semaphore: {shm.value}")
    shm.close()
