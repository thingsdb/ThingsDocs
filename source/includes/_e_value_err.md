## value_err

> This code shows ***value_err()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        value_err();
    ''', scope='@:stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q << EOQ "
value_err();
"
EOQ
```

> Return value in JSON format

```json
{
    "!": "value_err()",
    "error_code": -60,
    "error_msg": "object has the right type but an inappropriate value"
}
```

Returns an [error](#error-type).

This function does *not* generate an [event](#events).

### Function
`value_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | raw (optional) | Alternative error message.

### Return value
An error value.
