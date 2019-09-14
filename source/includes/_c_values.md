## values

> This code shows how to use `values()`:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        {a: 1, b: 2, c: 3}.values();
    ''', scope='@:stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q << EOQ "
{a: 1, b: 2, c: 3}.values();
"
EOQ
```

> Return value in JSON format (Warning: the order is *NOT* guaranteed)

```json
[
    1,
    2,
    3
]
```

Returns an array with all the property values of a [thing](#thing).
The same could be returned using map so the following statement is `true`:

`(.values() == .map(|_, v| v))`

<aside class="warning">
Although the <code>values()</code> and <code>map()</code> in the example above will return an array with the same order,
the order of <i>values</i> in the array is not guaranteed and may be different each time you run the query.
</aside>


This function does *not* generate an [event](#events).

### Function
*thing*.`values()`

### Arguments
None

### Return value
Returns an array with property values.
