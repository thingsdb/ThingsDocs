## pop

> This code show an example usage of ***pop()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        (arr = [1.2.3]).pop();
        arr;
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
(arr = [1, 2, 3]).pop();
arr;
"
EOQ
```

> Return value in JSON format

```json
[
    3,
    [
        1,
        2
    ]
]
```

Removes the last element from an [array](#array-type) and returns that element.
This method changes the length of the array. The `pop()` method works
on a `list` type array, but not on a `tuple` since tuples are immutable.

This function generates an [event](#events).

### Function
*list*.`pop()`

### Arguments
None

### Return value
The removed element from the array. An `INDEX_ERROR` is raised if the array is empty.