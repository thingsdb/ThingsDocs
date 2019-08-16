## refs
> Returns the reference count of a given value:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        [
            refs( 'some string' ),
            refs( a = b = c = 42 ),
        ];
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
[
    refs( 'some string' ),
    refs( a = b = c = 42 ),
];
"
EOQ
```

> Example return value in JSON format

```json
[
    2,
    5
]
```

Returns the reference count of a value.

The count returned is generally one higher than you might expect,
because it includes the (temporary) reference.

<aside class="notice">
Different nodes might return different reference values since the reference counter
can be higher of lower depending on how the value is stored and used.
</aside>

This function does *not* generate an [event](#events).

### Function
`refs(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to return the reference count for.

### Return value
Reference count of the given value.