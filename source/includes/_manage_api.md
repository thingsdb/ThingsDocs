# Manage API
ThingsDB can be managed with simple query commands. This allows you to manage
collections, users, nodes and view statistics about the active nodes.
All manage queries should use target `0` which is the `root` of ThingDB.


## collection

This function does *not* generate an [event](#events).

## collections

This function does *not* generate an [event](#events).

## counters

This function does *not* generate an [event](#events).

## del_collection

> This code will delete collection *old_things*:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    # Delete collection `old_things`
    await client.del_collection('old_things')

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# Delete collection `old_things`
thingscmd -n node.local -u admin -p pass -q << EOQ "
del_collection('old_things');
"
EOQ
```

Delete a collection.

This function generates an [event](#events).

### Function
`del_collection(name);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
name | raw (required) | Name of the collection to delete.


## del_user

This function generates an [event](#events).

## grant

grant access.

This function generates an [event](#events).

## new_collection

> This code will create a collection *"awesome_things"*:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    await client.new_collection('awesome_things')

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# Creates a new collection
thingscmd -n node.local -u admin -p pass -q << EOQ "
new_collection('awesome_things');
"
EOQ
```

> Example return value in JSON format (the new collection id)

```json
31415
```

Create a new collection.

This function generates an [event](#events).

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


## new_node

This function generates an [event](#events).

## new_user

This function generates an [event](#events).

## node

This function does *not* generate an [event](#events).

## nodes

This function does *not* generate an [event](#events).

## pop_node

This function generates an [event](#events).

## rename_collection

This function generates an [event](#events).

## rename_user

This function generates an [event](#events).

## reset_counters

This function does *not* generate an [event](#events).

## revoke

revoke access.

This function generates an [event](#events).

## set_loglevel

This function does *not* generate an [event](#events).

## set_password

> This code changes the password for use *admin*:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
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

Change a users password.

This function generates an [event](#events).

### Function
`set_password(username, new_password);`

### Arguments
Argument | Type | Description
--------- | ----------- | -----------
username | raw (required) | Name of the user
new_password | raw (required) | New password, can be anything from 1 to 128 graphical characters

### Return value
Returns `nil` if successful. An `INDEX_ERROR` is returned
if the user does not exist and `BAD_REQUEST` if the new password is not compliant.


## set_quota

This function generates an [event](#events).

## set_zone

This function does *not* generate an [event](#events).

## shutdown

This function does *not* generate an [event](#events).

## user

This function does *not* generate an [event](#events).

## users

This function does *not* generate an [event](#events).
