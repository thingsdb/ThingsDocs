## assert_err

> This code shows ***assert_err()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        assert_err()
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
assert_err();
"
EOQ
```

> Return value in JSON format

```json
{
    "!": "assert_err()",
    "error_code": -50,
    "error_msg": "assertion statement has failed"
}
```

Returns an [error](#error-type).

This function does *not* generate an [event](#events).

### Function
`assert_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | raw (optional) | Alternative error message.

### Return value
An error value.
