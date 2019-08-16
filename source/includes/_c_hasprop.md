## hasprop

> This code shows an example use case of ***hasprop()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        $tmp = {name: 'Iris'};
        $tmp.hasprop('name');
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
\$tmp = {name: 'Iris'};
\$tmp.hasprop('name');
"
EOQ
```

> Return value in JSON format

```json
true
```

Determines if a [thing](#thing) has a given property.

This function does *not* generate an [event](#events).

### Function
*thing*.`hasprop(property)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
property | raw (required) | Name of the property to check.

### Return value
Returns `true` the given property is found and otherwise `false`.
