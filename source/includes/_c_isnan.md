## isnan

> This code shows some return values for ***isnan()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        [
            isnan( true ),
            isnan( 123 ),
            isnan( 3.14 ),
            isnan( inf ),
            isnan( [] ),
            isnan( {} ),
            isnan( nan ),
            isnan( '123' ),
        ];
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
[
    isnan( true ),
    isnan( 123 ),
    isnan( 3.14 ),
    isnan( inf ),
    isnan( [] ),
    isnan( {} ),
    isnan( nan ),
    isnan( '123' ),
];
"
EOQ
```

> Return value in JSON format

```json
[
    false,
    false,
    false,
    false,
    true,
    true,
    true,
    true
]
```

This function determines whether the value passed to this function is a number.

This function does *not* generate an [event](#events).

### Function
`isnan(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value
Returns `true` is the given value is not a number, else `false`.
