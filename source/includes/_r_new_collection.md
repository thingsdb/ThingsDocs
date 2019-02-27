## new_collection

> This code will create a collection *"awesome_things"*:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        new_collection('awesome_things');
    ''')
    print(res)

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
Returns the new collection `id` if successful. An `INDEX_ERROR` is raised
if the collection already exists.
