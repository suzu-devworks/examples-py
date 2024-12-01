import mmap

import posix_ipc


def run(name: str) -> None:
    shm = posix_ipc.SharedMemory(name, flags=posix_ipc.O_CREAT, size=20, read_only=False)
    mm = mmap.mmap(shm.fd, shm.size)
    shm.close_fd()

    print(f"write to {name}")
    try:
        while True:
            text = input("Please enter something:")
            # Since the last position is referenced at the time of opening,
            # the reference position is returned.
            mm.seek(0)
            mm.write(text.encode(encoding="utf-8"))
            mm.write(b"\n")
            mm.write(b"\0") # For the unexpected
            print(f"write: {text}")

    except KeyboardInterrupt:
        print("canceled.")
        pass

    mm.close()
