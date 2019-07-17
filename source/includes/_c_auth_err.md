## auth_err

> This code shows ***auth_err()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        auth_err()
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
auth_err();
"
EOQ
```

> Return value in JSON format

```json
{
    "!": "auth_err()",
    "error_code": -56,
    "error_msg": "authentication error"
}
```

Returns an [error](#error-type).

This function does *not* generate an [event](#events).

### Function
`auth_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | raw (optional) | Alternative error message.

### Return value
An error value.
