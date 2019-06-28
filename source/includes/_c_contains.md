## endswith

> This code shows an example using ***contains()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        'the answer to life the universe and everything'.contains('life');
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
'the answer to life the universe and everything'.contains('life');
"
EOQ
```

> Return value in JSON format

```json
true
```

Determines if a given string is a substring of a string.

This function does *not* generate an [event](#events).

### Function
*string*.`contains(search_string)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
search_string | raw (required) | The characters to be searched for in the string.

### Return value
Returns `true` the given characters are found as a substring and otherwise `false`.

