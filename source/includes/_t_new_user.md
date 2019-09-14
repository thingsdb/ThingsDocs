## new_user

> Create a new user `iris` with password `siri`:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        new_user('iris');
    ''')
    print(res)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -q << EOQ "
new_user('iris');
"
EOQ
```

> Example return value in JSON format (the new user id)

```json
19
```

Creates a new user to ThingsDB. The new user is created without a password, token and access privileges.
You probably want to [set a password](#set_password) or add a [new token](#new_token) and assign some privileges using [grant(...)](#grant).

This function generates an [event](#events).

### Function
`new_user(user);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
`user` | raw (required) | Username, between 1 and 128 *graphical* characters.

### Return value
Returns the new user `id` if successful. An `INDEX_ERROR` is raised
if the user already exists.
