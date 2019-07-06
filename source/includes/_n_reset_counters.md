## reset_counters

> This code will reset the counters on a node:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    client.authenticate(auth=['admin', 'pass'])
    # resets counters on `node.local:9200`
    res = await client.query(r'''
        reset_counters();
    ''')
    print(res)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# resets counters on `node.local:9200`
thingscmd -n node.local -u admin -p pass -q << EOQ "
reset_counters();
"
EOQ
```

> Example return value in JSON format (the new collection id)

```json
null
```

Resets the [counters](#counters) for the ThingsDB node you are connected too.
Other nodes are not affected.

This function does *not* generate an [event](#events).

### Function
`reset_counters();`

### Arguments
None

### Return value
Returns `nil`.
