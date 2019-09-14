## map

> This code shows an example using ***map()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        users = [{name: 'Iris', age: 6}, {name: 'Sasha', age: 34}];

        /* returns ['Iris', 'Sasha'] */
        users.map(|user| user.name);
    ''', scope='@:stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q << EOQ '
users = [{name: "Iris", age: 6}, {name: "Sasha", age: 34}];

// returns ["Iris", "Sasha"]
users.map(|user| user.name);
'
EOQ
```

> Return value in JSON format

```json
[
    "Iris",
    "Sasha"
]
```

Iterate over items in an [array](#array-type), [set](#set-type) or over all properties on a [thing](#thing-type).

<aside class="warning">
Be aware that the order when iterating over a <i>set</i> or a <i>thing</i> is not guaranteed.
</aside>


This function does *not* generate an [event](#events).

### Function
*iterable*.`map(callback)`

### Arguments
Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
array    | item, index | Iterate over all items in the array. Both item and index are optional.
set      | thing, id   | Iterate over things in the set. Both `thing` and `id` are optional.
thing    | name, value | Iterate over the thing properties. Both name and value are optional.

### Return value
A new array with each element being the result of the callback function.
