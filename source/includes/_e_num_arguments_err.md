## num_arguments_err

> This code shows ***num_arguments_err()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        num_arguments_err();
    ''', scope='@:stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q << EOQ "
num_arguments_err();
"
EOQ
```

> Return value in JSON format

```json
{
    "!": "num_arguments_err()",
    "error_code": -62,
    "error_msg": "wrong number of arguments"
}
```

Returns an [error](#error-type).

This function does *not* generate an [event](#events).

### Function
`num_arguments_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | raw (optional) | Alternative error message.

### Return value
An error value.
