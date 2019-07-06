## new_node

> Create a new node in zone `0`:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    # ThingsDB must be started on node2 using the `--secret ...` argument
    await client.connect('node1.local')
    client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        new_node('my-one-time-serect', 'node2.local');
    ''')
    print(res)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# ThingsDB must be started on node2 using the `--secret ...` argument
thingscmd -n node.local -u admin -p pass -q << EOQ "
new_node('my-one-time-serect', 'node2.local');
"
EOQ
```

> Example return value in JSON format (the new node id)

```json
1
```

Adds a new node to ThingsDB. Nodes are used for scaling and high availability.


This function generates an [event](#events).

### Function
`new_node(secret, ip_address [, port]);`


### Arguments
Argument | Type | Description
-------- | ---- | -----------
`secret` | raw (required) | Secret used to initially connect to the new node.
`ip_address` | raw (required) | IP Address (IPv4 or IPv6) of the new node.
`port` | int (optional) | Node port (`listen_node_port`), an integer between 0 an 65535, default **9220**.


### Return value
Returns the new node `id` if successful.