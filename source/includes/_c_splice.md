## splice

> This code replaces an element in a list at position 2:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        months = ['Jan', 'Feb', 'April'];
        months.splice(2, 1, 'March');       /* Returns: ['April'] */
        months;
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
months = ['Jan', 'Feb', 'April'];
months.splice(2, 1, 'March');       /* Returns: ['April'] */
months;
"
EOQ
```

> Return value in JSON format

```json
[
    "Jan",
    "Feb",
    "March"
]
```

The `splice()` method changes the contents of an array by removing or replacing
existing elements and/or adding new elements in place.

This function generates an [event](#events).

### Function
*list*.`splice(start, [delete_count, [item1, item2, ..., itemX]])`)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
start | int (required) | Start index in the array. If negative, it will begin that many elements from the end of the array.
delete_count | int (optional) | Number of item to remove from `start`. If `<= 0`, no items will be removed.
item1, item2, ..., itemX | any (optional) | Items to add, beginning from `start`.

### Return value
An array containing the deleted elements. If only one element is removed,
an array of one element is returned. If no elements are removed, an empty array is returned.