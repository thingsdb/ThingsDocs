## test

> Examples using ***test()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        [
            'Hello world!!'.test(/^hello/),
            'Hello world!!'.test(/^hello/i),
        ];
    ''', scope='@:stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q << EOQ "
[
    'Hello world!!'.test(/^hello/),
    'Hello world!!'.test(/^hello/i),
];
"
EOQ
```

> Return value in JSON format

```json
[
    false,
    true
]
```

Test if a string matches a given [regular expression](#regex) and return `true` or `false`.

This function does *not* generate an [event](#events).

### Function
*string*.`test(regex)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
regex | regex (required) | The regular expression to test against the string.

### Return value
`true` if there is a match between the string and the specified regular expression, otherwise `false`.
