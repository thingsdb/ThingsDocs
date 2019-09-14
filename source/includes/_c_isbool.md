## isbool

> This code shows some return values for ***isbool()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        [
            isbool( true ),
            isbool( 'true' ),
            isbool( nil ),
        ];
    ''', scope='@:stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q << EOQ "
[
    isbool( true ),
    isbool( 'true' ),
    isbool( nil ),
];
"
EOQ
```

> Return value in JSON format

```json
[
    true,
    false,
    false
]
```

This function determines whether the value passed to this function
is a [bool](#boolean) or not.

This function does *not* generate an [event](#events).

### Function
`isbool(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value
Returns `true` is the passed value is a boolean else it returns `false`.
