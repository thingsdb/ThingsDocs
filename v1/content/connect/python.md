---
title: "Python"
weight: 12
---

### Installation

{{% notice note %}}
The **python-thingsdb** library requires **Python 3.10** or higher.
{{% /notice %}}

Just use pip:

```bash
pip install python-thingsdb
```

Or, clone the project and use setup.py:

```bash
python setup.py install
```

### Quick usage

```python
import asyncio
from thingsdb.client import Client


async def hello_world():
    client = Client()

    # replace `localhost` with your ThingsDB server address
    await client.connect('localhost')

    # WebSocket connection are also supported: (replace port if required)
    #
    #   await client.connect('ws://localhost:9270')
    #
    # for a secure connection, use wss:// and provide an SSL context, example:
    # (ssl can be set either to True or False, or an SSLContext)
    #
    #   client = Client(ssl=True)
    #   await client.connect('wss://localhost:9270')
    #

    try:
        # replace `admin` and `pass` with your username and password
        # or use a valid token string
        await client.authenticate('admin', 'pass')

        # perform the hello world code...
        # the //ti comment is optional to tell your IDE to use ThingsDB
        # syntax highlighting if supported.
        print(await client.query("""//ti
            "Hello World!";
        """))

    finally:
        # the will close the client in a nice way
        client.close()
        await client.wait_closed()

# run the hello world example
asyncio.run(hello_world())
```

### More info

A more complete description of the Python client can be found in one of the links below.

- https://github.com/thingsdb/python-thingsdb#readme
- https://pypi.org/project/python-thingsdb/
