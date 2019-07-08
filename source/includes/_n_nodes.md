## nodes

> This code returns info for all ThingsDB nodes:

```python
import asyncio
from thingsdb.client import Client, scope

async def example():
    await client.connect('node.local')
    client.authenticate(auth=['admin', 'pass'])
    res = await client.nodes()
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -s node -q << EOQ "
nodes();
"
EOQ
```

> Example return value in JSON format

```json
[
    {
        "address": "node.local",
        "committed_event_id": 5,
        "next_thing_id": 8,
        "node_id": 0,
        "port": 9220,
        "status": "READY",
        "stored_event_id": 5,
        "syntax_version": "v0"
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


This function does *not* generate an [event](#events).

### Function
`nodes()`

### Arguments
None

### Return value
Array containing information about each node.