## overflow_err

> This code shows ***overflow_err()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        overflow_err()
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
overflow_err();
"
EOQ
```

> Return value in JSON format

```json
{
    "!": "overflow_err()",
    "error_code": -59,
    "error_msg": "integer overflow"
}
```

Returns an [error](#error-type).

This function does *not* generate an [event](#events).

### Function
`overflow_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | raw (optional) | Alternative error message.

### Return value
An error value.
