## keys

> This code shows how to use `keys()`:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        {a: 1, b: 2, c: 3}.keys();
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
{a: 1, b: 2, c: 3}.keys();
"
EOQ
```

> Return value in JSON format

```json
[
    "a",
    "b",
    "c"
]
```

Returns an array with all the property names of a [thing](#thing).
The same could be returned using map so the following statement is `true`:

`(.keys() == .map(|k| k))`

This function does *not* generate an [event](#events).

### Function
*thing*.`keys()`

### Arguments
None

### Return value
Returns an array with property names.
