## max_quota_err

> This code shows ***max_quota_err()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        max_quota_err()
    ''', scope='@:stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q << EOQ "
max_quota_err();
"
EOQ
```

> Return value in JSON format

```json
{
    "!": "max_quota_err()",
    "error_code": -57,
    "error_msg": "max quota is reached"
}
```

Returns an [error](#error-type).

This function does *not* generate an [event](#events).

### Function
`max_quota_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | raw (optional) | Alternative error message.

### Return value
An error value.
