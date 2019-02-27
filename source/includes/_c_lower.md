## lower

> Example using ***lower()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        'Hello World!!'.lower();
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
'Hello World!!'.lower();
"
EOQ
```

> Return value in JSON format

```json
"hello world!!"
```

Return a new string in which all case-based characters are in lower case.

This function does *not* generate an [event](#events).

### Function
*string*.`lower()`
