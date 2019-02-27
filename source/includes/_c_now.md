## now

> This code shows the current timestamp:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    # current timestamp
    res = await client.query(r'''
        now();
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
# current timestamp
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
now();
"
EOQ
```

> Example return value in JSON format

```json
1551093313.6622682
```

Return the time in seconds since the epoch as a [floating point](#floating-point) number.

If you require the *same* time multiple times within a query,
then call `now()` only once and save it to a temporary variable, for example `$now = now();`

This function does *not* generate an [event](#events).


### Function
`now()`

### Arguments
None

### Return value
Current timestamp.