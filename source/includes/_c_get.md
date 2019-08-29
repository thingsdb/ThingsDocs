## get

> This code shows an example use case of ***get()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        tmp = {name: 'Iris'};
        tmp.get('name');
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
tmp = {name: 'Iris'};
tmp.get('name');
"
EOQ
```

> Return value in JSON format

```json
"Iris"
```

Return the value of a property on a [thing](#thing-type) by a given property name.

This function does *not* generate an [event](#events).

### Function
*thing*.`get(name)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
name | raw (required) | Name of the property where to return the value for.

### Return value
Returns the value for the given property name.
