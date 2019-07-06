## del_token

> This code will delete a token:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    client.authenticate(auth=['admin', 'pass'])
    # Delete a token
    await client.del_token('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# Delete a token
thingscmd -n node.local -u admin -p pass -q << EOQ "
del_token('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX');
"
EOQ
```

Delete a token.

This function generates an [event](#events).

### Function
`del_token(key);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
key | raw (required) | Token key to delete.
