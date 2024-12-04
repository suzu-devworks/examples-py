import posix_ipc


def run(name: str, count: int, release: bool) -> None:
    sem = posix_ipc.Semaphore(name, flags=posix_ipc.O_CREAT, initial_value=count)

    previous = sem.value
    if release:
        sem.release()
    else:
        sem.acquire(0)

    print(f"semaphore[{name}]: {previous} -> {sem.value}")
    sem.close()
