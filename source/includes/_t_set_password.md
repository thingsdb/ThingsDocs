## set_password

> This code changes the password for use *admin*:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    await client.set_password('admin', 'my_secret_password')

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# Change the password for user `admin`
thingscmd -n node.local -u admin -p pass -q << EOQ "
set_password('admin', 'my_secret_password');
"
EOQ
```

> Return value in JSON format

```json
null
```

Change a users password. This function can also be used to remove an existing
password by using `nil` as the new password.

Passwords must contain 1 to 128 printable characters.

This function generates an [event](#events).

### Function
`set_password(username, new_password);`

### Arguments
Argument | Type | Description
--------- | ----------- | -----------
username | raw (required) | Name of the user
new_password | nil/raw (required) | New password or `nil`

### Return value
Returns `nil` if successful. An `INDEX_ERROR` is returned
if the user does not exist and `BAD_REQUEST` if the new password is not compliant.
