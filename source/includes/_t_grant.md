## grant

> Grant read and watch privileges to user `iris` to collection `stuff`:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        new_user('iris');
        new_token('iris');
        [
            grant('.node', 'iris', WATCH),
            grant('stuff', 'iris', (READ|WATCH)),
        ];
    ''')
    print(res)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -q << EOQ "
new_user('iris');
new_token('iris');
[
    grant('.node', 'iris', WATCH),
    grant('stuff', 'iris', (READ|WATCH)),
];
"
EOQ
```

> Return value in JSON format

```json
[
    null,
    null
]
```

Grant collection or general privileges to a user. Access to a user is provided by setting
a bit mask to either the `.node` scope, `.thingsdb` scope or a collection.
Privileges to ThingsDB gives a user the ability to view counters, add, view remove users etc.

The following pre-defined masks are available:

Mask         | Description
------------ | -----------
`READ` (1)   | Gives read access.
`MODIFY` (2) | Gives read and modify access.
`GRANT` (4)  | Gives read, modify and grant (and revoke) privileges.
`WATCH` (8)  | Gives watch (and un-watch) privileges.
`RUN` (16)   | Gives run procedures access.
`FULL` (31)  | A *mask* for full privileges.

<aside class="notice">
It is not possible to have <code>GRANT</code> privileges without also having <code>MODIFY</code> privileges.
Similarly, it is not possible to have <code>MODIFY</code> privileges without <code>READ</code>.
</aside>


This function generates an [event](#events).

### Function
`grant(target, user, mask);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
`target` | int/raw | Can be either the `.node` scope, `.thingsdb` scope, or a collection name or id.
`user` | raw | User to grant privileges to.
`mask` | int | Bit-mask for setting privileges.

### Return value
Returns `nil` when successful. An `INDEX_ERROR` is raised if the user or target
does not exist.
