## rename

> This code renames property `world` to `universe`:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        world = 'huge';
        rename('world', 'universe');
        map(|k|k);
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
world = 'huge';
rename('world', 'universe');
map(|k|k);
"
EOQ
```

> Return value in JSON format

```json
[
    "universe"
]
```

Rename a property on a [thing](#thing). The *destination* property with value will be overwritten
if it already existed.

This function generates an [event](#events).

### Function
*thing*.`rename(current, dest)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
current | raw (required) | Name of the property to rename.
dest | raw (required) | New name of the property.

### Return value
Returns `nil` is the rename was successful.

