import json
import time

import posix_ipc


def run(name: str, count: int) -> None:
    mq = posix_ipc.MessageQueue(name, posix_ipc.O_CREAT)

    print(f"send to {name} {count} times.")
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

    mq.close()
    print("send complete.")
