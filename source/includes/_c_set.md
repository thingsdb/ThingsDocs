## set

> This code shows some return values for ***set()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        set([{}, {}]),
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
[
    set(),
    set([{}, {}]),
];
"
EOQ
```

> Return value in JSON format

```json
[
    {
        "!": []
    },
    {
        "!": [
            {
                "#": 0
            },
            {
                "#": 0
            }
        ]
    }
]
```

Returns a new empty [set](#set). If an array is given, then all elements in the
given array must be or type `thing` and a new set is returned based on the
given things.

This function does *not* generate an [event](#events).

### Function
`set([array])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
array | array (optional) | Optional array to initialize the set.

### Return value
A new set.
