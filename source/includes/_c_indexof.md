## indexof

> This code shows an example using ***indexof()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        users.indexof(t(42));
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
users.indexof(t(42));
"
EOQ
```

> Example return value in JSON format when `t(42)` was found at the 7th place, so at index 6.

```json
6
```

Returns the first index at which a given value can be found in the [array](#array-type), or `nil` if it is not present.
The index of an array starts at `0`, so the first item has index `0` the second `1` and so on.

This function does *not* generate an [event](#events).

### Function
*array*.`indexof(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any | The value to find the index for.

### Return value
Index at which the first item matches a given value, or `nil` if it is not present.
