## has

> This code shows an example use case of ***has()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        $iris = {name: 'Iris'};
        $set = set([$iris]);

        /* Check if $iris is in the set */
        $set.has($iris);
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
\$iris = {name: 'Iris'};
\$set = set([\$iris]);

/* Check if $iris is in the set */
\$set.has(\$iris);
"
EOQ
```

> Return value in JSON format

```json
true
```

Determines if a [set](#set) has a given thing.

This function does *not* generate an [event](#events).

### Function
*set*.`has(thing)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
thing | thing (required) | Thing to check.

### Return value
Returns `true` the given thing is found in the set and otherwise `false`.
