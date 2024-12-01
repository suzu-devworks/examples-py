import json
import time
from datetime import datetime

import posix_ipc


def run(name: str) -> None:
    mq = posix_ipc.MessageQueue(name, posix_ipc.O_CREAT)

    print(f"start queue server: {name}")
    try:
        while True:
            now = datetime.now().time()
            message = mq.receive()
            print(now, json.loads(message[0]))
            time.sleep(1)

    except KeyboardInterrupt:
        print("canceled.")
        pass

    mq.close()
    print(f"end queue server: {name}")
