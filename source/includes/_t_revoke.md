## revoke

> Revoke all privileges for user `iris` on collection `stuff`:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        revoke('stuff', 'iris', FULL);
    ''')
    print(res)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -q << EOQ "
revoke('stuff', 'iris', FULL);
"
EOQ
```

> Return value in JSON format

```json
null
```

Revoke collection or general privileges from a user. See [grant](#grant) for more information on
how access privileges can be set for a user.

This function generates an [event](#events).

### Function
`revoke(target, user, mask);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
`target` | int/raw | Can be either the `:node` scope, `:thingsdb` scope, or a collection name or id.
`user` | raw | User to revoke privileges from.
`mask` | int | Bit-mask for revoking privileges.

### Return value
Returns `nil` when successful. An `INDEX_ERROR` is raised if the user or target
does not exist.
