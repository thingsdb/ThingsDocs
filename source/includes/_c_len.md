## len

> This code uses `len()` to return the number of items in a collection:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        len();
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
[1, 2, 3, 4].len();
"
EOQ
```

> Return value in JSON format

```json
4
```

Returns the length of an [array](#array-type) or [string](#string-raw), or the number of items in a [thing](#thing).

This function does *not* generate an [event](#events).

### Function
*iterable*.`len()`

### Arguments
None

### Return value
Returns length of the iterable.
