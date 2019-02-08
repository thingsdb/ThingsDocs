## blob

> This code assigns the ThingsDB logo to an attribute *logo* using a blob:

```python
import asyncio
import urllib
from thingsdb.client import Client

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    stuff = await client.get_collection('stuff')

    # TODO: replace with ThingsDB logo
    resp = urllib.request.urlopen(
        'https://upload.wikimedia.org/wikipedia/commons/1/15/Siridb-logo.svg')

    # The python client will automatically use a blob for byte values
    await stuff.set('logo', resp.read())

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
# Note: thingscmd supports only one blob per query, so this is always blob(0)
wget 'https://upload.wikimedia.org/wikipedia/commons/1/15/Siridb-logo.svg' | \
thingscmd -n node.local -u admin -p pass -c stuff -q "set('logo', blob(0));"
```

Blobs can be used to send binary data to ThingsDB. Each query request allows you to send
an array of *blob* values together with the query. Within the query it is then possible
to use this function to *get* the blob value.

This function does *not* generate an [event](#events).

### Function
`blob(index)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
index | int (required) | Index of a blob in the blobs array. This value may be negative, for example: `-1` can be used to get the last blob in the array.

### Return value
Returns the blob. An `INDEX_ERROR` is returned
if the blob at the given `index` does not exist.