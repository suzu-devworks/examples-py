import mmap

import posix_ipc


def run(name: str, size: int) -> None:
    shm = posix_ipc.SharedMemory(name, flags=posix_ipc.O_CREAT, size=size, read_only=False)
    mm = mmap.mmap(shm.fd, shm.size)
    shm.close_fd()

    print(f"write to {name}")
    try:
        while True:
            text = input("Please enter something:")
            # Since the last position is referenced at the time of opening,
            # the reference position is returned.
            mm.seek(0)
            mm.write(b"\0" * mm.size())  # null clear.
            mm.seek(0)
            mm.write(text.encode(encoding="utf-8"))
            print(f"write: {text}")

    except KeyboardInterrupt:
        print("canceled.")
        pass

    mm.close()
