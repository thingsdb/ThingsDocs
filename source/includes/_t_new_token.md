## new_token

> Create a new token for user `admin`:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    # ThingsDB must be started on node2 using the `--secret ...` argument
    await client.connect('node1.local')
    client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        new_token('admin', now() + 7*24*3600, 'token for one week');
    ''')
    print(res)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# ThingsDB must be started on node2 using the `--secret ...` argument
thingscmd -n node.local -u admin -p pass -q << EOQ "
new_token('admin', now() + 7*24*3600, 'token for one week');
"
EOQ
```

> Example return value in JSON format (the token key)

```json
"FXIxyVAJmtQ8o5GTU8yZxdsKrZC7TRijzZ71Kh5q"
```

Adds a new token for a given user. An optional expiration time may be given after which the token cannot
be used anymore. Use [del_expired](#del_expired) to cleanup expired tokens. The expiration time may be
given as a UNIX time-stamp in seconds or a date/time string.

Some valid date/time strings:

- `2021-01-01`
- `2023-02-06 14:30`
- `2023-07-5T13:23:20+01:00`

Expiration dates in the past are not allowed an will raise a `BAD_REQUEST` error.

It is also possible to set a description for the token which can be used to identify where token is used for.
If you only want to set a description, but no expiration time, then you can use `nil` as second argument.
For example: `new_token('my_user', nil, 'some nice description');`

There can be no more than 128 tokens assigned to a single user. A `MAX_QUOTA_ERROR` is raised if this limit
is reached. Existing tokens can be removed with [del_token](#del_token) and to view the current tokens you can use the [user(..)](#user) (or [users()](#users)) function.

This function generates an [event](#events).

### Function
`new_token(username, [, expiration_time] [, description]);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
username | raw (required) | Name of the user.
expiration_time | nil/int/float/raw (optional) | Expiration date of the token.
description | raw (optional) | Token description.

### Return value
Returns the new token key.
