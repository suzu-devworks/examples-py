# examples-ipc

This project is about learning about the capabilities and usage of messaging using posix ipc.

## Table of Contents <!-- omit in toc -->

- [examples-ipc](#examples-ipc)
  - [Getting Started](#getting-started)
    - [POSIX IPC message queues](#posix-ipc-message-queues)
    - [POSIX IPC shared memory](#posix-ipc-shared-memory)
    - [POSIX IPC semaphore](#posix-ipc-semaphore)
  - [References](#references)

## Getting Started  

Install dependency packages and install myself locally:

```shell
rye sync
```

### POSIX IPC message queues

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
examples-ipc posix mqueue --clean -n /test
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

### POSIX IPC shared memory

Start the server:

```shell
examples-ipc posix shm -s -n /test
```

Read the shared memory every 3 second.

```console
start shared memory server: /test
14:38:54.422853 
...
```

Start the client:

```shell
examples-ipc posix shm -n /test
```

The client will wait for input.

```console
write to /test-shm
Please enter something: hello,world{enter}
```

When you enter some text on the client and press Enter, that text is written to the shared memory.

Displays what you type in the server console:

```console
...
14:51:43.439146
14:51:46.440134 hello,world
14:51:49.445372 hello,world
...
```

Unlike C, when reading shared memory we use a little trick to write only one line of text because it is not NULL terminated (It's a bit of a lack of consideration).

To delete a POSIX queue:

```shell
examples-ipc posix shm --clean -n /test
```

You can also check the shared memory with the command:

```shell
cat /dev/shm/{shared-memory-name}
```

### POSIX IPC semaphore

Start the server:

```shell
examples-ipc posix semaphore -s -n /test
```

Check the semaphore value every 3 seconds.

```console
start semaphore server: /test size: 2
09:49:30.469668 semaphore: 1
09:49:31.470277 semaphore: 1
...
```

Run the client:

```shell
examples-ipc posix semaphore -n /test
```

The semaphore value on the server console will be decreased by 1.

```console
...
09:54:12.219855 semaphore: 1
09:54:13.221488 semaphore: 0
...
```

If the semaphore is 0, the client fails.

```console
<class 'posix_ipc.BusyError'> Semaphore is busy
```

Running the client with `--release` will increment the semaphore by 1.

```shell
examples-ipc posix semaphore -n /test --release
```

The semaphore value on the server changes.

```console
...
10:01:39.183558 semaphore: 0
10:01:40.188027 semaphore: 1
...
```

## References

- <https://pypi.org/project/posix-ipc/>
