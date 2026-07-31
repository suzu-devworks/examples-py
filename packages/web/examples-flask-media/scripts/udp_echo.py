"""Echo server for UDP communication.

Examples:
    Starting the server::

    ```shell
    python ./scripts/udp_echo.py 5502
    ```

    Request from client::

    ```shell
    echo "TEST" | nc -u 127.0.0.1 5502
    ```

"""

import argparse
import socket


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Echo server for UDP communication")
    p.add_argument("port", type=int, nargs="?", default=5501, help="The server listens to port")
    p.add_argument("-b", "--bind", default="127.0.0.1", help="Address to bind")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    udp_host = args.bind
    udp_port = args.port

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
    sock.bind((udp_host, udp_port))
    print(f"Listening on UDP://{udp_host}:{udp_port}")

    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        print(addr, ":", data)


if __name__ == "__main__":
    main()
