# Manage ThingsDB
ThingsDB can be managed with simple query commands. This allows you to manage
collections, users, nodes and view statistics about the active nodes.
All manage queries should use target `0` which is the `root` of ThingDB.


## New Collection

> This code will create a collection *"awesome_things"*:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('localhost', 9200)
    await client.authenticate('iris', 'siri')
    await client.new_collection('awesome_things')

asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -u username -p password -s server.local -c << EOQ

/* Creates a new collection */
new_collection('awesome_things');

EOQ
```

Create a new collection.

### Function
`new_collection(name);`

### Arguments
Argument | Type | Description
--------- | ----------- | -----------
name | raw (required) | Name of the new collection.

<aside class="notice">
The user who has created the collection will automatically be granted full
access rights to the new collection.
Use <code>grant</code> to give other users access to the
collection.
</aside>

## Grant

grant access.