import json
import time

import posix_ipc


def run(queue_name: str, count: int) -> None:
    # posix_ipc.unlink_message_queue(queue_name)
    mq = posix_ipc.MessageQueue(queue_name, posix_ipc.O_CREAT)

    print(f"send to {queue_name} {count} times.")
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
