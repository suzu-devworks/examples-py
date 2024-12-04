import sysv_ipc


def run(key: int, size: int) -> None:
    shm = sysv_ipc.SharedMemory(key, sysv_ipc.IPC_CREAT, size=size)

    print(f"write to {key}")
    try:
        while True:
            text = input("Please enter something:")
            shm.write("\0" * shm.size)
            shm.write(text.encode(encoding="utf-8"))
            print(f"write: {text}")

    except KeyboardInterrupt:
        print("canceled.")
        pass

    # shm.close()
