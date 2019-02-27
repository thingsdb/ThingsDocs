## find

> This code shows an example using ***find()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        users.find(user => user.name.startswith('Jeroen'));
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
users.find(user => user.name.startswith('Jeroen'));
"
EOQ
```

> Example return value in JSON format

```json
{
    "#": 16,
    "email": "jeroen@transceptor.technology",
    "name": "Jeroen van der Heijden"
}
```

This function returns the value of the first element in the array or thing that satisfies the callback function.
Otherwise `nil` is returned.

This function does *not* generate an [event](#events).

### Function
*iterable*.`find(callback)`

### Arguments
Explanation of the *callback* argument:

Iterable | Callback | Description
-------- | -------- | -----------
array | item, index => ... | Iterate over items in the array. Both item and index are optional.
thing | name, value => ... | Iterate over thing properties. Both name and value are optional.

### Return value
The value of the first element in the array or thing that satisfies the provided testing function;
otherwise, `nil` is returned.
