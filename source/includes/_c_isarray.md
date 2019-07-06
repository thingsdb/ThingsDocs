## isarray

> This code shows some return values for ***isarray()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        [
            isarray( [] ),
            isarray( $tmp = [['nested']] ),
            isarray( $tmp[0] ),
        ];
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
[
    isarray( [] ),
    isarray( \$tmp = [['nested']] ),
    isarray( \$tmp[0] ),
];
"
EOQ
```

> Return value in JSON format

```json
[
    true,
    true,
    true
]
```

This function determines whether the value passed to this function
is an [array](#array-type) type or not. The functions [islist](#islist) and
[istuple](#istuple) can be used to check if the array is mutable.

This function does *not* generate an [event](#events).

### Function
`isarray(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested for being an array.

### Return value
Returns `true` the value passed is array else it returns `false`.
