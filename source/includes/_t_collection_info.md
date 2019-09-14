## collection_info
> Returns information about collection *stuff*:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.collection_info("stuff")
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -q << EOQ "
collection_info('stuff');
"
EOQ
```

> Example return value in JSON format

```json
{
    "collection_id": 782,
    "name": "stuff",
    "quota_array_size": null,
    "quota_properties": null,
    "quota_raw_size": null,
    "quota_things": null,
    "things": 61352
}
```

Returns information about a specific collection.

This function does *not* generate an [event](#events).