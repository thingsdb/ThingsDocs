## extend

> This code extends a list with a given array:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        a = [1, 2, 3];
        b = [4, 5, 6];
        a.extend(b);  // returns the new length, 6
        a;
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ '
a = [1, 2, 3];
b = [4, 5, 6];
a.extend(b);  // returns the new length, 6
a;
'
EOQ
```

> Return value in JSON format

```json
[
    1,
    2,
    3,
    4,
    5,
    6
]
```

Adds an array with items to the end of a list, and returns the new length.

This function generates an [event](#events).

### Function
*list*.`extend(array)`

### Return value
Returns the new length of the list.