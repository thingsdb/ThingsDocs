## raise

> This code shows how ***raise()*** can be used:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        raise ();
        'This code is not reached';
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
raise ();
'This code is not reached';
"
EOQ
```

Raises an [error](#error-type).

This function does *not* generate an [event](#events).

### Function
`raise([error])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | error (optional) | The error to raise.

### Return value
None