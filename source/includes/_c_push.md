## push

> This code pushes values to a list:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        list = [1, 2, 3];
        list.push(4, 5, 6);
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
list = [1, 2, 3];
list.push(4, 5, 6);
"
EOQ
```

> Return value in JSON format

```json
6
```

Adds new items to the end of an array, and returns the new length.

This function generates an [event](#events).

### Function
*list*.`push(item1, item2, ..., itemX)`

### Return value
Returns the new length of the list.