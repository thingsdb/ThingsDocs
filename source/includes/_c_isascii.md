## isascii

> This code shows some return values for ***isascii()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        [
            isascii( 'ԉ' ),
            isascii( 'pi' ),
        ];
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
[
    isascii( 'ԉ' ),
    isascii( 'pi' ),
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

This function determines whether the value passed to this function is of
type `raw` and contains only valid ascii characters.

This function does *not* generate an [event](#events).

### Function
`isascii(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value
Returns `true` is the given value is of type `raw` and contains only ascii characters, else `false`.
