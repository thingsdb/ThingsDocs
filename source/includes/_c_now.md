## now

> This code shows the current timestamp:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    # current timestamp in float and milliseconds
    res = await client.query(r'''
        $now = now();
        $now;
        int($now);
        int(($now * 1000));
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
# current timestamp in float and milliseconds
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
\$now = now();
\$now;
int(\$now);
int((\$now * 1000));
"
EOQ
```

> Example return value in JSON format

```json
[
    null,
    1550221210.3550816,
    1550221210,
    1550221210355
]
```

Returns the current timestamp as [float](#floating-point).

If you require the *same* timestamp multiple times within a query,
then call `now()` only once and save it to a temporary variable, for example `$now = now();`

This function does *not* generate an [event](#events).


### Function
`now()`

### Arguments
None

### Return value
Current timestamp.