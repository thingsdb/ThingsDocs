## del_expired

> This code will delete all expired tokens:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    # Delete all expired tokens
    await client.del_expired()

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# Delete all expired tokens
thingscmd -n node.local -u admin -p pass -q << EOQ "
del_expired();
"
EOQ
```

Delete all expired tokens.

This function generates an [event](#events).

### Function
`del_expired();`

### Arguments
None

### Return value
Returns `nil`.