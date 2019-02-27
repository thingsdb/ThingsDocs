## startswith

> This code shows an example using ***startswith()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        'the answer to life the universe and everything'.startswith('the answer');
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
'the answer to life the universe and everything'.startswith('the answer');
"
EOQ
```

> Return value in JSON format

```json
true
```

Determines if a string starts with characters given by another string.

This function does *not* generate an [event](#events).

### Function
*string*.`startswith(search_string)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
search_string | raw (required) | The characters to be searched for at the start of this string.

### Return value
Returns `true` the given characters are found at the start of the string and otherwise `false`.
