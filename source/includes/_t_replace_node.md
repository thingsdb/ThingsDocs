## replace_node

> Replace node with id 1:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    # node3.local must be started using the `--secret ...` argument
    # and the node with id 1 must be turned off
    await client.connect('node1.local')
    client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        replace_node(1, 'my-one-time-serect', 'node3.local');
    ''')
    print(res)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# node3.local must be started using the `--secret ...` argument
# and the node with id 1 must be turned off
thingscmd -n node.local -u admin -p pass -q << EOQ "
replace_node(1, 'my-one-time-serect', 'node3.local');
"
EOQ
```

> Return value in JSON format

```json
null
```

Replace a node in ThingsDB. This can be used if an existing node has a
unrecoverable state, for example a hardware failure. This function requires
a node id as its first argument which can be queried using the [nodes_info()](#nodes_info)
function.


This function generates an [event](#events).

### Function
`replace_node(node_id, secret, ip_address [, port]);`


### Arguments
Argument | Type | Description
-------- | ---- | -----------
`node_id` | int (required) | Node id of the node to replace.
`secret` | raw (required) | Secret used to initially connect to the new node.
`ip_address` | raw (required) | IP Address (IPv4 or IPv6) of the new node.
`port` | int (optional) | Node port (`listen_node_port`), an integer between 0 an 65535, default **9220**.


### Return value
Returns `nil` if successful.