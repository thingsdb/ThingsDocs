## refs
> Returns the reference of a thing:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        t = {};
        t.refs();
        {}.refs();
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
t = {};
t.refs();
{}.refs();
"
EOQ
```

> Return value in JSON format

```json
[
    null,
    2,
    1
]
```

Returns the reference count of the [thing](#thing).

The count returned is generally one higher than you might expect,
because it includes the (temporary) reference.

This function does *not* generate an [event](#events).

### Function
`*thing*.ref()`

### Arguments
None

### Return value
Reference count of the thing.