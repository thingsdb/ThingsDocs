## isutf8

> This code shows some return values for ***isutf8()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        isutf8( 'ԉ' );
        isutf8( 'pi' );
    ''', target='stuff', all_=True)
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -a -q << EOQ "
isutf8( 'ԉ' );
isutf8( 'pi' );
"
EOQ
```

> Return value in JSON format

```json
[
    true,
    true
]
```

This function determines whether the value passed to this function is of
type `raw` and contains valid utf8.

This function does *not* generate an [event](#events).

### Function
`isutf8(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value
Returns `true` is the given value is of type `raw` and contains valid utf8, else `false`.
