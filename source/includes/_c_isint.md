## isint

> This code shows some return values for ***isint()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        isint( 42 );
        isint( 0x2a );
        isint( 42.0 );
        isint( '42' );
        isint( true );
    ''', target='stuff', all=True)
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -a -q << EOQ "
isint( 42 );
isint( 0x2a );
isint( 42.0 );
isint( '42' );
isint( true );
"
EOQ
```

> Return value in JSON format

```json
[
    true,
    true,
    false,
    false,
    false
]
```

This function determines whether the value passed to this function
is an [integer](#integer) or not.

This function does *not* generate an [event](#events).

### Function
`isint(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value
Returns `true` is the passed value is an integer else it returns `false`.
