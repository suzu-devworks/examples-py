import json
import time

import sysv_ipc


def run(key: int, count: int) -> None:
    mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)

    print(f"send to {key} {count} times.")
    try:
        for i in range(count):
            counter = i
            obj = {"count": counter}
            mq.send(json.dumps(obj))
            print(f"pushed: {counter}")
            time.sleep(1)

    except KeyboardInterrupt:
        print("canceled.")
        pass

    # mq.close()
    print("send complete.")
