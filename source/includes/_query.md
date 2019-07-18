# Query

> Example query

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect(
        'node.local',       # node address
        9200                # node port, default 9200
    )
    await client.authenticate(auth=[
        'admin',            # username
        'pass',             # password
    ])
    res = await client.query(
        "'Hello world!!'",  # query string
        target=client.node, # collection or scope, defaults to client.thingsdb
    )
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd \
    --node        node.local \
    --user        admin      \
    --password    pass       \
    --scope       node       \
    --query       "'Hello world!!'"
```

> Request in JSON format

```json
{
    "query": "'Hello world!!'",
    "collection": "stuff",
    "blobs": []
}
```

Queries to ThingsDB can be used to manage [nodes](#node-api), [ThingsDB](#thingsdb-api) or to query [collections](#collection-api).

ThingsDB will respond with the last statement result. In case a statement fails, the other statements are
not processed and an [error](#errors) is returned. Changes will be synchronized to all nodes and optionally to watchers,
even when an error has ocurred.

A query request has a required field *query*, and a required field *collection* when querying a collection scope.


Key | Type | Description
--- | ---- | -----------
`query` | string | The query string containing one or more statements. (required)
`collection` | string| Required only in the collection scope.
`blobs` | array | (Only the collection scope) Additional blobs for binary data. (default: `[]`)

To send a query you can either use a language binding, see code examples, or if you
want to know how to serialize and send the data, read the [protocol](#protocol) section.