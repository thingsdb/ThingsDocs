## findindex

> This code shows an example using ***findindex()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        users.findindex(|user| user.name.startswith('Jeroen'));
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
users.findindex(|user| user.name.startswith('Jeroen'));
"
EOQ
```

> Example return value in JSON format

```json
42
```

This function returns the index of the first element in an [array](#array-type) that satisfies the callback function.
Otherwise `nil` is returned.

This function does *not* generate an [event](#events).

### Function
*array*.`findindex(callback)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
callback | closure | The statement to try.

Explanation of the *callback* argument:

Iterable | Callback arguments | Description
-------- | -------- | -----------
array | item, index | Iterate over items in the array. Both item and index are optional.


### Return value
The index of the first element in the array or thing that satisfies the provided testing function;
otherwise, `nil` is returned.
