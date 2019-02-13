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