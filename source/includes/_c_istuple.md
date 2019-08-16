## istuple

> This code shows some return values for ***istuple()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        [
            istuple( [] ),
            istuple( $tmp = [['nested'], set()] ),
            istuple( $tmp[0] ),
            istuple( $tmp[1] ),
        ];
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
[
    istuple( [] ),
    istuple( \$tmp = [['nested'], set()] ),
    istuple( \$tmp[0] ),
    istuple( \$tmp[1] ),
];
"
EOQ
```

> Return value in JSON format

```json
[
    false,
    false,
    true,
    true
]
```

This function determines whether the value passed to this function
is a immutable [array](#array-type) or not. At least nested arrays are of kind tuple.

This function does *not* generate an [event](#events).

### Function
`istuple(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value
Returns `true` is the passed value is a tuple else it returns `false`.
