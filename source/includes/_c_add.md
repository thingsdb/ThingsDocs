## add

> This code adds things to a set:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        s = set(); a = {item: 'a'}; b = {item: 'b'};
        s.add(a, a, b);
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
s = set(); a = {item: 'a'}; b = {item: 'b'};
s.add(a, a, b);
"
EOQ
```

> Return value in JSON format

```json
2
```

Adds new thing to the [set](#set-type) and returns the number of things which are
actually added to the set. For example `my_set.add( t(42) );` will return `0`
if `my_set` already contains thing `#42`.

This function generates an [event](#events).

### Function
*set*.`add(thing1, thing1, ..., thingX)`

### Return value
Returns the number of `things` which are added to the set.