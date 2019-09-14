## nodes_info

> This code returns info for all ThingsDB nodes:

```python
import asyncio
from thingsdb.client import Client, scope

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.nodes_info()
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s node -q << EOQ "
nodes_info();
"
EOQ
```

> Example return value in JSON format

```json
[
    {
        "address": "localhost",
        "committed_event_id": 5,
        "next_thing_id": 8,
        "node_id": 0,
        "port": 9220,
        "status": "READY",
        "stored_event_id": 5,
        "syntax_version": "v0",
        "zone": 0,
    }
]
```

Returns information about all ThingsDB nodes.

Value | Description
------- | -----------
address | IP address or hostname of the node.
committed_event_id | Last known committed event ID on the node.
next_thing_id | Next free thing ID on the node.
node_id | ID which is assigned to the node.
port | TCP port on which the node is listening for node connections.
status | Current status of the node.
stored_event_id | Last known stored event ID on the node.
syntax_version | Language or syntax version which is running on the node.
zone | Zone number to which the node is assigned.


This function does *not* generate an [event](#events).

### Function
`nodes_info()`

### Arguments
None

### Return value
Array as `qpack` type containing node information for all nodes within ThingsDB.
