import sysv_ipc


def run(key: int) -> None:
    shm = sysv_ipc.SharedMemory(key, sysv_ipc.IPC_CREAT, size=20)

    print(f"write to {key}")
    try:
        while True:
            text = input("Please enter something:")
            shm.write(text.encode(encoding="utf-8"))
            print(f"write: {text}")

    except KeyboardInterrupt:
        print("canceled.")
        pass

    # shm.close()
