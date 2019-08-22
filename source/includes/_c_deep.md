## deep

> This code uses `deep()` to return the default `deep` value:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        deep();  // returns the default since `deep` is not changed
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
deep();  // returns the default since `deep` is not changed
"
EOQ
```

> Return value in JSON format

```json
1
```

Returns the current `deep` value. The `deep` value might change when a function with a [return(..)](#return) is called which has changed the `deep` value for this query.

This function does *not* generate an [event](#events).

### Function
`deep()`

### Arguments
None

### Return value
The current `deep` value for the running query.
