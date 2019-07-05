## new_user

> Create a new user `iris` with password `siri`:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        new_user('iris', 'siri');
    ''')
    print(res)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -q << EOQ "
new_user('iris', 'siri');
"
EOQ
```

> Example return value in JSON format (the new user id)

```json
19
```

Creates a new user to ThingsDB. The new user is created without any access privileges.
, so probably you also
want to assign some privileges to the new user by using [grant(...)](#grant).

This function generates an [event](#events).

### Function
`new_user(user, password);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
`user` | raw (required) | Username, between 1 and 128 *graphical* characters.
`password` | raw (required) | Password for the new user, between 1 and 128 *printable* characters.

### Return value
Returns the new user `id` if successful. An `INDEX_ERROR` is raised
if the user already exists.
