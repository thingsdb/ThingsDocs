## array

> This code shows some return values for ***array()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        array( set( [{}, {}] ) );
    ''', scope='@:stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q << EOQ "
array( set( [{}, {}] ) );
"
EOQ
```

> Return value in JSON format

```json
[
    {},
    {}
]
```

Returns a new empty [array](#array-type) or returns an array for a given `set`.

This function does *not* generate an [event](#events).

### Function
`array([set])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
set | set (optional) | Optional set to initialize the array.

### Return value
A new array.
