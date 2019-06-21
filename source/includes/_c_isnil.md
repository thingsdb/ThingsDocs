## isnil

> This code shows some return values for ***isnil()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        isnil( nil );
        isnil( 0 );
    ''', target='stuff', all_=True)
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -a -q << EOQ "
isnil( nil );
isnil( 0 );
"
EOQ
```

> Return value in JSON format

```json
[
    true,
    false
]
```

This function determines whether the value passed to this function is [nil](#nil).

This function does *not* generate an [event](#events).

### Function
`isnil(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value
Returns `true` is the given value is `nil`, else `false`.
