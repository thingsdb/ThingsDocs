# Query

> Example query

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect(
        'localhost',       # node address
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
    --node        localhost \
    --user        admin      \
    --password    pass       \
    --scope       @thingsdb  \
    --query       "'Hello world!!'"
```

> Request in JSON format

```json
["@thingsdb", "'Hello world!!'"]
```

Queries to ThingsDB can be used to manage [nodes](#node-api), [ThingsDB](#thingsdb-api) or to query [collections](#collection-api).

A query request has a required field *scope* and *query*, and an option required field *collection* when querying a collection scope.


To send a query you can either use a language binding, see code examples, or if you
want to know how to serialize and send the data, read the [protocol](#protocol) section.