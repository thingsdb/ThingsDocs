## ret

> This code show how to use function ***ret()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        ($tmp = 'just an example, returns nil').ret();
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
(\$tmp = 'just an example, returns nil').ret();
"
EOQ
```

> Return value in JSON format

```json
null
```

Use this function to simply return `nil`. This can be useful in some cases
where you don't want to return the default value from some function to prevent
unnecessary network traffic.

This function does *not* generate an [event](#events).

### Function
*value*.`ret()`

### Return value
Returns `nil`.

