## type
> Returns the type name of a given value:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        [
            type( nil ),
            type( 42 ),
            type( 3.14 ),
        ];
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
[
    type( nil ),
    type( 42 ),
    type( 3.14 ),
];
"
EOQ
```

> Example return value in JSON format

```json
[
    "nil",
    "int",
    "float"
]
```

Returns the type name of a value.

This function does *not* generate an [event](#events).

### Function
`type(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to return the type name for.

### Return value
Type name of the given value.