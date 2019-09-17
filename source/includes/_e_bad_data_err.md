## bad_data_err

> This code shows ***bad_data_err()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        bad_data_err();
    ''', scope='@:stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q << EOQ "
bad_data_err();
"
EOQ
```

> Return value in JSON format

```json
{
    "!": "bad_data_err()",
    "error_code": -53,
    "error_msg": "unable to handle request due to invalid data"
}
```

Returns an [error](#error-type).

This function does *not* generate an [event](#events).

### Function
`bad_data_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | raw (optional) | Alternative error message.

### Return value
An error value.
