---
title: "Python"
weight: 10
---

### Installation

{{% notice note %}}
The **python-thingsdb** library requires **Python 3.6** or higher.
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

    try:
        # replace `admin` and `pass` with your username and password
        # or use a valid token string
        await client.authenticate('admin', 'pass')

        # perform the hello world code...
        print(await client.query('''
            "Hello World!";
        '''))

    finally:
        # the will close the client in a nice way
        client.close()
        await client.wait_closed()

# run the hello world example
asyncio.get_event_loop().run_until_complete(hello_world())
```

### More info

A more complete description of the Python client can be found in one of the links below.

- https://github.com/thingsdb/python-thingsdb#readme
- https://pypi.org/project/python-thingsdb/
