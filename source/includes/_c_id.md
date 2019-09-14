## id

> This code uses `id()` to return a collection id:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        .id();  // Returns the collection id
    ''', scope='@:stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q << EOQ '
.id();  // Returns the collection id
'
EOQ
```

> Example return value in JSON format

```json
3
```

Returns the `id` of a [thing](#thing-type) or `nil` if the thing is not stored.

This function does *not* generate an [event](#events).

### Function
*thing*.`id()`

### Arguments
None

### Return value
Returns `id` of a thing or `nil` when the thing is not stored.
