## endswith

> This code shows an example using ***endswith()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        'the answer to life the universe and everything'.endswith('everything');
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
'the answer to life the universe and everything'.endswith('everything');
"
EOQ
```

> Return value in JSON format

```json
true
```

Determines if a string ends with characters given by another string.

This function does *not* generate an [event](#events).

### Function
*string*.`endswith(search_string)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
search_string | raw (required) | The characters to be searched for at the end of this string.

### Return value
Returns `true` the given characters are found at the end of the string and otherwise `false`.

