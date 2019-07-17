## node_err

> This code shows ***node_err()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        node_err()
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
node_err();
"
EOQ
```

> Return value in JSON format

```json
{
    "!": "node_err()",
    "error_code": -51,
    "error_msg": "node is temporary unable to handle the request"
}
```

Returns an [error](#error-type).

This function does *not* generate an [event](#events).

### Function
`node_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | raw (optional) | Alternative error message.

### Return value
An error value.
