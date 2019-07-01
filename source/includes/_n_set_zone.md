## set_zone

> This code will set the zone to `1` on `node.local:9200`:

```python
import asyncio
from thingsdb.client import Client, scope

client = Client()

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    # set the zone to 1 on 'node.local:9200'
    res = await client.query(r'''
        set_zone(1);
    ''', target=scope.node)
    print(res)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# returns counters for 'node.local:9200'
thingscmd -n node.local -u admin -p pass -s node -q << EOQ "
set_zone(1);
"
EOQ
```

> Return value in JSON format

```json
null
```

This function sets the zone on the connected ThingsDB node.

Each node can be placed in a zone which is represented by an integer value between `0` and `255`.
By default each node is placed into zone `0`. Zones are used when a query is forwarded by a node
to another node to outsource some work. The *other* node is selected randomly from all available
nodes, but nodes in the same zone are preferred.

So when do you configure a zone for a node? In case nodes are spread across multiple locations, you might
want to configure the nodes in the same location or region with a specified zone number to reduce
network traffic time when forwarding packages from one node to another.

This function does *not* generate an [event](#events).

### Function
`set_zone(zone);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
zone | integer (required) | Integer value between `0` and `255` representing the zone number.

### Return value
Returns `nil`.
