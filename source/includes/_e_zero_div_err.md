## zero_div_err

> This code shows ***zero_div_err()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        zero_div_err()
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
zero_div_err();
"
EOQ
```

> Return value in JSON format

```json
{
    "!": "zero_div_err()",
    "error_code": -58,
    "error_msg": "division or module by zero"
}
```

Returns an [error](#error-type).

This function does *not* generate an [event](#events).

### Function
`zero_div_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | raw (optional) | Alternative error message.

### Return value
An error value.
