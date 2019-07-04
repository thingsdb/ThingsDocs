## grant

> Grant read and watch privileges to user `iris` to collection `stuff`:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        grant('stuff', 'iris', (READ|WATCH));
    ''')
    print(res)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -q << EOQ "
grant('stuff', 'iris', (READ|WATCH));
"
EOQ
```

> Return value in JSON format

```json
null
```

Grant collection or general privileges to a user. Access to a user is provided by setting
a bit mask to either the `:node` scope, `:thingsdb` scope or a collection.
Privileges to ThingsDB gives a user the ability to view counters, add, view remove users etc.

The following pre-defined masks are available:

Mask | Description
---- | -----------
`READ` (1) | Gives read access.
`MODIFY` (3) | Gives read and modify access.
`WATCH` (4) | Gives watch (and un-watch) privileges.
`GRANT` (11) | Gives read, modify and grant(/revoke) privileges.
`FULL` (15) | Gives full privileges.


This function generates an [event](#events).

### Function
`grant(target, user, mask);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
`target` | int/raw | Can be either the `:node` scope, `:thingsdb` scope, or a collection name or id.
`user` | raw | User to grant privileges to.
`mask` | int | Bit-mask for setting privileges.

### Return value
Returns `nil` when successful. An `INDEX_ERROR` is raised if the user or target
does not exist.
