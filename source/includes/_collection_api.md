# Collection API

> This code returns the *id* of collection *stuff*

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query('id()', scope='@:stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q 'id()'
```

The functions in the Collection API can also be used in the [thingsdb](#thingsdb-api) and [node](#node-api) scopes.
