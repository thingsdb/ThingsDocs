## islist

> This code shows some return values for ***islist()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        [
            islist( [] ),
            islist( $tmp = [['nested']] ),
            islist( $tmp[0] ),
        ];
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
[
    islist( [] ),
    islist( \$tmp = [['nested']] ),
    islist( \$tmp[0] ),
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
is a mutable [array](#array-type) or not.

This function does *not* generate an [event](#events).

### Function
`islist(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value
Returns `true` is the passed value is a `list`, else it returns `false`.
