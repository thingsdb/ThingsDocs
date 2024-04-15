---
title: "WebSocket"
weight: 24
---


To use WebSockets, at least one node within your cluster must have the WebSocket port enabled, as it's disabled by default.
To activate it, edit the `ws_port` setting in your ThingsDB [configuration file](https://github.com/thingsdb/ThingsDB/blob/main/thingsdb.example.conf)
or set the `THINGSDB_WS_PORT` environment variable. You can use a common port like `9270` for this purpose.

When enabled, connections can be made using `ws://<address>:<port>`.

## Enabling Secure WebSockets

To safeguard data transfer with Secure WebSockets, certificates are essential.

For testing, one can create certificates using the following commands:

Generate private key (.key)
Key considerations for algorithm "RSA" ≥ 2048-bit
```
openssl genrsa -out server.key 2048
```
Key considerations for algorithm "ECDSA" (X25519 || ≥ secp384r1)
https://safecurves.cr.yp.to/
List ECDSA the supported curves (openssl ecparam -list_curves)
```
openssl ecparam -genkey -name secp384r1 -out server.key
```
Generation of self-signed(x509) public key (PEM-encodings .pem|.crt) based on the private (.key)
```
openssl req -new -x509 -sha256 -key server.key -out server.crt -days 3650
```

Configure the `ws_key_file` and `ws_cert_file` settings in your configuration file or `THINGSDB_WS_KEY_FILE` and `THINGSDB_WS_CERT_FILE` environment variable.

Once configured, establish connections using the secure protocol: `wss://<addess>:<port>`.

## Using ThingsDB WebSockets

The easiest option is to use an existing _connector_ with WebSocket support.

The following connectors are available:

Language                 | Query/Run support | Room (event) support
------------------------ | ----------------- | --------------------
[Python](../python)       | &#x2714;          | &#x2714;


### Implement WebSocket for a new language

Do you want to implement WebSockets

**Connection Similarities:** WebSocket connections mirror reading and writing to a [socket](../socket), but with a dedicated framework for handling WebSocket protocols.

Example pseudo code:

```python
websocket = connect("ws://localhost:9720")  # Establish WebSocket connection
data = msgpack.pack(['admin', 'pass'])  # Package data using MessagePack

# Craft the header:
header = header.pack(
    len(data),  # Size: Unsigned 32-bit integer (little endian)
    0,          # Package ID: 16-bit value
    33,         # Type: Unsigned 8-bit value
    33 ^ 0xff)  # Check: Unsigned 8-bit value (XOR calculation for integrity)

# Transmit header and data:
websocket.send(header + data)

# Receive response:
resp = websocket.recv()  # Await server response

# Process response data ...
```

For in-depth details on processing response data and crafting messages, refer to the dedicated [socket documentation](../socket) section.
