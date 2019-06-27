## isfloat

> This code shows some return values for ***isfloat()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        [
            isfloat( 42.0 ),
            isfloat( 0.42e+2 ),
            isfloat( 42 ),
        ];
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
[
    isfloat( 42.0 ),
    isfloat( 0.42e+2 ),
    isfloat( 42 ),
];
"
EOQ
```

> Return value in JSON format

```json
[
    true,
    true,
    false
]
```

This function determines whether the value passed to this function
is a [floating point](#floating-point) value or not.

This function does *not* generate an [event](#events).

### Function
`isfloat(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value
Returns `true` is the passed value is a float else it returns `false`.
