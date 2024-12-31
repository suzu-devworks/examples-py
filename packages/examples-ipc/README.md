# examples-ipc

This project is about learning about the capabilities and usage of messaging using posix ipc.

## Table of Contents <!-- omit in toc -->

- [examples-ipc](#examples-ipc)
  - [References](#references)
  - [Getting Started](#getting-started)
    - [POSIX IPC message queue](#posix-ipc-message-queue)
    - [POSIX IPC shared memory](#posix-ipc-shared-memory)
    - [POSIX IPC semaphore](#posix-ipc-semaphore)
    - [SystemV IPC message queue](#systemv-ipc-message-queue)
    - [SystemV IPC shared memory](#systemv-ipc-shared-memory)
    - [SystemV IPC semaphore](#systemv-ipc-semaphore)
  - [Development](#development)
    - [How the project was initialized](#how-the-project-was-initialized)

## References

- <https://pypi.org/project/posix-ipc/>
- <https://pypi.org/project/sysv-ipc/>

## Getting Started  

Install dependency packages:

```shell
uv sync
```

### POSIX IPC message queue

It doesn't matter whether you start the server or the client first.

Start the server:

```shell
examples-ipc posix msq -s -n /test
```

Start the client:

```shell
examples-ipc posix msq -n /test -c 15
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

To delete a POSIX message queue:

```shell
examples-ipc posix msq --clean -n /test
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
04:44:28.716438 
04:44:31.722418 
...
```

Start the client:

```shell
examples-ipc posix shm -n /test
```

The client will wait for input.

```console
write to /test-shm
Please enter something: {input here}
```

When you enter some text on the client and press Enter, that text is written to the shared memory.

Displays what you type in the server console:

```console
...
04:46:28.896235 
04:46:31.897707 hello,world
04:46:34.903215 hello,world
...
```

To delete a POSIX shared memory:

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
examples-ipc posix sem -s -n /test
```

Checks the semaphore value every second and notifies you if there is a change.

```console
start semaphore server: /test size: 2
08:00:22.925505 semaphore: 2
```

Run the client:

```shell
examples-ipc posix sem -n /test
```

The semaphore value on the server console will be decreased by 1.

```console
...
08:00:22.925505 semaphore: 2
08:01:41.174018 semaphore: 1
```

If the semaphore is 0, the client fails.

```console
<class 'posix_ipc.BusyError'> Semaphore is busy
```

Running the client with `-r` or `--release` will increment the semaphore by 1.

```shell
examples-ipc posix sem -n /test -r
```

The semaphore value on the server changes.

```console
...
08:01:57.223437 semaphore: 0
08:02:15.274874 semaphore: 1
```

### SystemV IPC message queue

The behavior is the same as POSIX, so please check there.
In SystemV, they are identified by numbers rather than names.

Start the server:

```shell
examples-ipc sysv msq -s -k 200
```

Start the client:

```shell
examples-ipc sysv msq -k 200 -c 15
```

To delete a SystemV message queue:

```shell
examples-ipc sysv msq --clean -k 200
```

You can check the status of the queue with the following command:

```shell
ipcs -q
```

<!-- /* spell-checker:disable */ -->
```console
------ Message Queues --------
key        msqid      owner      perms      used-bytes   messages    
0x000000c8 1          vscode     600        0            0 
```
<!-- /* spell-checker:enable */ -->

### SystemV IPC shared memory

The behavior is the same as POSIX, so please check there.

Start the server:

```shell
examples-ipc sysv shm -s -k 200
```

Start the client:

```shell
examples-ipc sysv shm -k 200
```

To delete a SystemV shared memory:

```shell
examples-ipc sysv shm --clean -k 200
```

You can also check the shared memory with the command:

```shell
ipcs -m
```

<!-- /* spell-checker:disable */ -->
```console
------ Shared Memory Segments --------
key        shmid      owner      perms      bytes      nattch     status      
0x000000c8 1          vscode     600        20         0         
```
<!-- /* spell-checker:enable */ -->

### SystemV IPC semaphore

If a POSIX semaphore exists, it will be acquired as is,
but be aware that if you add an initialization parameter in SystemV, it will be overwritten.

This example requires that you start the server first.

Start the server:

```shell
examples-ipc sysv sem -s -k 200
```

Run the client:

```shell
examples-ipc sysv sem -k 200

# or 

examples-ipc sysv sem -k 200 -r
```

The semaphore values ​​displayed on the server seem to be different from the POSIX semaphore values, so there may be significant differences in functionality between semaphores.

To delete a SystemV shared memory:

```shell
examples-ipc sysv shm --clean -k 200
```

You can also check the shared memory with the command:

```shell
ipcs -s
```

<!-- /* spell-checker:disable */ -->
```console
------ Semaphore Arrays --------
key        semid      owner      perms      nsems     
0x000000c8 2          vscode     600        1   
```
<!-- /* spell-checker:enable */ -->

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
uv init --package packages/examples-ipc
uv add --project packages/examples-ipc posix-ipc sysv-ipc
```
