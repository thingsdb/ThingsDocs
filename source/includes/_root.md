# Manage ThingsDB
ThingsDB can be managed with simple query commands. This allows you to manage
collections, users, nodes and view statistics about the active nodes.
All manage queries should use target `0` which is the `root` of ThingDB.


## Set Password

> This code changes the password for use *admin*:
```python

import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('localhost', 9200)
    await client.authenticate('admin', 'pass')
    await client.set_password('admin', 'my_secret_password')

asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -u admin -p pass -s server.local -q << EOQ "
/* Change the password for user `admin` */
set_password('admin', 'my_secret_password');
"
EOQ
```

> Example return value (just the new collection id)

```json
31415
```


## New Collection

> This code will create a collection *"awesome_things"*:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('localhost', 9200)
    await client.authenticate('admin', 'pass')
    await client.new_collection('awesome_things')

asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -u admin -p pass -s server.local -q << EOQ "
/* Creates a new collection */
new_collection('awesome_things');
"
EOQ
```

> Example return value (just the new collection id)

```json
31415
```

Create a new collection.
This function requires an [event](#events).

### Function
`new_collection(name);`

### Arguments
Argument | Type | Description
--------- | ----------- | -----------
name | raw (required) | Name of the new collection.

<aside class="notice">
The user who has created the collection will automatically receive full
access rights to the new collection.
Use <code>grant</code> to give other users access to the collection.
</aside>

### Return value
Returns the new collection `id` if successful. An `INDEX_ERROR` is returned
if the collection already exists.

## Delete Collection

> This code will delete collection *old_things*:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('localhost', 9200)
    await client.authenticate('admin', 'pass')
    await client.del_collection('old_things')

asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -s server.local -u admin -p pass -q << EOQ "
/* Delete a collection */
del_collection('old_things');
"
EOQ
```

Delete a collection.
This function requires an [event](#events).

### Function
`new_collection(name);`

### Arguments
Argument | Type | Description
--------- | ----------- | -----------
name | raw (required) | Name of the new collection.

<aside class="notice">
The user who has created the collection will automatically receive full
access rights to the new collection.
Use <code>grant</code> to give other users access to the collection.
</aside>

## Grant

grant access.