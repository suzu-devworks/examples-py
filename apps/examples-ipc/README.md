# examples-ipc

This project is about learning about the capabilities and usage of messaging using posix ipc.

## Table of Contents <!-- omit in toc -->

- [examples-ipc](#examples-ipc)
  - [Getting Started](#getting-started)
    - [Learn POSIX IPC message queues](#learn-posix-ipc-message-queues)
  - [References](#references)

## Getting Started  

Install dependency packages and install myself locally:

```shell
rye sync
```

### Learn POSIX IPC message queues

It doesn't matter whether you start the server or the client first.

Start the server:

```shell
examples-ipc posix mqueue -s -n /test
```

Start the client:

```shell
examples-ipc posix mqueue -n /test -c 15
```

If you start both, messages from the client will appear on the server console:

```console
09:39:41.019485 {'count': 1}
09:39:42.025510 {'count': 2}
09:39:43.027236 {'count': 3}
09:39:44.031384 {'count': 4}
09:39:45.037533 {'count': 5}
09:39:46.043485 {'count': 6}
09:39:47.048131 {'count': 7}
09:39:48.050594 {'count': 8}
09:39:49.056254 {'count': 9}
09:39:50.057588 {'count': 10}
09:39:51.058542 {'count': 11}
09:39:51.058542 {'count': 12}
09:39:51.058542 {'count': 13}
09:39:51.058542 {'count': 14}
```

To delete a POSIX queue:

```shell
examples-ipc --clean -n /test
```

You can check the status of the queue with the following command:

```shell
cat /dev/mqueue/{queue-name}
```

<!-- /* spell-checker:disable */ -->
```console
QSIZE:120        NOTIFY:0     SIGNO:0     NOTIFY_PID:0     
```
<!-- /* spell-checker:enable */ -->

## References

- <https://pypi.org/project/posix-ipc/>
