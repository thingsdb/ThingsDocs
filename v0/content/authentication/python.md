---
title: "Python"
weight: 2
---

> Use pip to install the python client:

```
pip install python-thingsdb
```

The Python client supports both queries, watching and a framework for using ThingsDB in a really simple way.

> To authorize in Python, use this code:

```python
import asyncio
from thingsdb.client import Client

client = Client()
loop = asyncio.get_event_loop()


async def example():
    # replace `localhost` with your ThingsDB server address
    await client.connect('localhost')

    # replace `amdin` with yout username and `pass` with your password
    await client.authenticate('admin', 'pass')

    # ..or by using a token
    await client.authenticate('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

# run the example
loop.run_until_complete(example())

# the will close the client in a nice way
client.close()
loop.run_until_complete(client.wait_closed())
```
