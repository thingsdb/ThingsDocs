# Collection API

> This code returns the *id* of collection *stuff*

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query('id()', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q 'id()'
```

The functions in the Collection API can also be used in the [thingsdb](#thingsdb-api) and [node](#node-api) scopes.
