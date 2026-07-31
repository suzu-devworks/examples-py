# Quick start - How-to guides

## Table of Contents <!-- omit in toc -->

- [Quick start](#quick-start)
  - [Say “Hello world!”](#say-hello-world)
  - [Encrypt connections](#encrypt-connections)
  - [Connect from a browser](#connect-from-a-browser)
  - [Broadcast messages](#broadcast-messages)
  - [Manage application state](#manage-application-state)

## Quick start

Learn about Websockets with QuickStart on the official website.

> [!WARNING]
> However, this tutorial has disappeared from the latest version of the website.

- [Quick start - websockets :link:](https://websockets.readthedocs.io/en/14.0/howto/quickstart.html)

### Say “Hello world!”

Start the server:

```shell
python examples/quickstart/01_say_hello_world/server.py
```

The client connects to the server and receives the response:

```shell
python examples/quickstart/01_say_hello_world/client.py
```

### Encrypt connections

The connection is encrypted with TLS (Transport Layer Security),
wss requires certificates like https.

We'll use the development TLS certificate here

Start the server:

```shell
python examples/quickstart/02_encrypt_connections/server_secure.py
```

The client connects to the server and receives the response:

```shell
python examples/quickstart/02_encrypt_connections/client_secure.py
```

> [!CAUTION] Configure the TLS context securely
> Please review the advice and security considerations in the documentation of
  the [ssl](https://docs.python.org/3/library/ssl.html#security-considerations)
  module to configure the TLS context securely.

### Connect from a browser

Start the websockets server:

```shell
python examples/quickstart/03_connect_from_a_browser/show_time.py
```

Start the http server:

```shell
python -m http.server 8000
```

Access from your browser:

- <http://localhost:8000/>

Search for `show_time.html` in the displayed directory view and display it.

### Broadcast messages

Start the websockets server:

```shell
python examples/quickstart/04_broadcast_messages/show_time_2.py
```

Start the http server:

```shell
python -m http.server 8000
```

Access from your browser:

- <http://localhost:8000/>

Display the `show_time.html` page as in the previous example

### Manage application state

Start the server:

```shell
python examples/quickstart/05_manage_application_state/counter.py
```

Start the http server:

```shell
python -m http.server 8000
```

Accessing a URL using multiple browsers:

- <http://localhost:8000/examples/quickstart/counter.html>
