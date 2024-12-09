import json
import signal
import time
from datetime import datetime
from typing import Any

import sysv_ipc


def handler(_signum: int, _frame: Any) -> None:
    # spell-checker:words signum
    pass


def run(key: int) -> None:
    signal.signal(signal.SIGINT, handler)

    mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)

    print(f"start queue server: {key}")
    try:
        while True:
            message = mq.receive()
            now = datetime.now().time()
            print(now, json.loads(message[0]))
            time.sleep(1)

    except sysv_ipc.Error:
        print("canceled.")
        pass

    # mq.close()
    print(f"end queue server: {key}")
