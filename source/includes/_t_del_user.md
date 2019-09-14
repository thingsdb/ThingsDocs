## del_user

> This code will delete user *test*:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    # Delete user `test`
    await client.del_user('test')

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# Delete user `test`
thingscmd -n localhost -u admin -p pass -q << EOQ "
del_user('test');
"
EOQ
```

Delete a user. It is not possible to delete your own user account and a `BAD_REQUEST` will be raised in case you try to.
Any *tokens* associated with the user will also be deleted.

This function generates an [event](#events).

### Function
`del_user(username);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
username | raw (required) | Username of the user to delete.

### Return value
Returns `nil` when successful. An `INDEX_ERROR` is raised if the user does not exist.
