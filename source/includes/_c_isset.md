## isset

> This code shows some return values for ***isset()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        [
            isset( [] ),
            isset( set() ),
        ];
    ''', scope='@:stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q << EOQ "
[
    isset( [] ),
    isset( set() ),
];
"
EOQ
```

> Return value in JSON format

```json
[
    false,
    true
]
```

This function determines whether the value passed to this function
is a [set](#set-type) or not.

This function does *not* generate an [event](#events).

### Function
`isset(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value
Returns `true` is the passed value is a `set`, else it returns `false`.
