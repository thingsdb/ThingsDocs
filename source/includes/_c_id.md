## id

> This code uses `id()` to return a collection id:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        id();
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
id();
"
EOQ
```

> Example return value in JSON format

```json
3
```

Returns the `id` of a [thing](#thing).

This function does *not* generate an [event](#events).

### Function
*thing*.`id()`

### Arguments
None

### Return value
Returns `id` of a thing.
