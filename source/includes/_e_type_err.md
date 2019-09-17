## type_err

> This code shows ***type_err()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        type_err();
    ''', scope='@:stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q << EOQ "
type_err();
"
EOQ
```

> Return value in JSON format

```json
{
    "!": "type_err()",
    "error_code": -61,
    "error_msg": "object of inappropriate type"
}
```

Returns an [error](#error-type).

This function does *not* generate an [event](#events).

### Function
`type_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | raw (optional) | Alternative error message.

### Return value
An error value.
