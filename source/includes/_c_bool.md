## bool

> This code shows some return values for ***bool()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        [
            bool(),
            bool(nil),
            bool({}),
            bool({answer: 42}),
            bool([]),
            bool([1, 2, 3]),
            bool(''),
            bool('forty two'),
        ];
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
[
    bool(),
    bool(nil),
    bool({}),
    bool({answer: 42}),
    bool([]),
    bool([1, 2, 3]),
    bool(''),
    bool('forty two'),
];
"
EOQ
```

> Return value in JSON format

```json
[
    false,
    false,
    false,
    true,
    false,
    true,
    false,
    true
]
```

Returns an [bool](#boolean) from a specified value.
If no value is given, `false` is returned.

Types with a *length* evaluate to `true` when the length is *not* `0` and `false` otherwise.

This function does *not* generate an [event](#events).

### Function
`bool(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (optional) | The value where to return a boolean value for.

### Return value
A boolean value.
