## counters

> This code will return node counter values:

```python
import asyncio
from thingsdb.client import Client, scope

client = Client()

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    # returns counters for `node.local:9200`
    res = await client.query(r'''
        counters();
    ''', target=scope.node)
    print(res)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# returns counters for `node.local:9200`
thingscmd -n node.local -u admin -p pass -s node -q << EOQ "
counters();
"
EOQ
```

> Example return value in JSON format

```json
{
    "average_event_duration": 3.368566710075053e-05,,
    "events_committed": 80352,
    "events_failed": 0,
    "events_killed": 0,
    "events_quorum_lost": 0,
    "events_skipped": 0,
    "events_unaligned": 0,
    "events_with_gap": 0,
    "garbage_collected": 0,
    "longest_event_duration": 3.508100053295493e-05,
    "queries_received": 130944
}
```

Returns `counters` for the ThingsDB node you are connected too. Counters start all at zero when ThingsDB
is started, or when the counters are reset by using [reset_counters()'](#reset-counters).

Counters give information about things, queries and events. If you suspect failed queries, then
counters might provide you with more information.

Counter | Description
------- | -----------
average_event_duration | The average event duration in seconds.
events_committed | Events committed since last counters reset.
events_failed | Failed events. This is a critical counter which should be 0.
events_killed | Killed events took too long for receiving the `READY` status. These event may be processed later.
events_quorum_lost | Number of times a quorum was not received.
events_skipped | Events which cannot be committed since an event with a higher `id` is already processed. These events are moved to a skipped queue.
events_unaligned | Number of times an event cannot be pushed to the end of the queue and needs re-ordering.
events_with_gap | Events which are committed but at least one event `id` was skipped.
garbage_collected | Number of things which are garbage collected.
longest_event_duration | Longest event duration, in seconds.
queries_received | Number of queries where this node acted as the master node.

This function does *not* generate an [event](#events).

### Function
`counters();`

### Arguments
None

### Return value
Returns the current counter values.
