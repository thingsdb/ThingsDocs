## isthing

> This code shows some return values for ***isthing()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        [
            isthing( {} ),
            isthing( [] ),
        ];
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
[
    isthing( {} ),
    isthing( [] ),
];
"
EOQ
```

> Return value in JSON format

```json
[
    true,
    false
]
```

This function determines whether the value passed to this function
is a [thing](#thing) or not.

This function does *not* generate an [event](#events).

### Function
`isthing(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value
Returns `true` is the passed value is a thing else it returns `false`.
