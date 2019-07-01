## float

> This code shows some return values for ***float()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        [
            float(),
            float(42),
            float('0.365e+3 days'),
            float('0xFF'),
            float(true),
            float(false),
        ];
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
[
    float(),
    float(42),
    float('0.365e+3 days'),
    float('0xFF'),
    float(true),
    float(false),
];
"
EOQ
```

> Return value in JSON format

```json
[
    0,
    42.0,
    365.0,
    255.0,
    1.0,
    0.0
]
```

Returns a [float](#floating-point) from a specified value.
If no value is given, the default float `0.0` is returned.

If the specified value is of type [raw](#string-raw), then the initial characters
of the string are converted until a non-digit character is found.
Initial white space is ignored and the number may start with an optional `+` or `-` sign.

Type [bool](#boolean) values are converted to `1.0` for `true` and `0.0` for `false`.

This function does *not* generate an [event](#events).

### Function
`float(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (optional) | The value where to create a floating point value for.

### Return value
A floating point value. Other type than `float`, `raw`, `bool` or `int`
will raise a `BAD_REQUEST`.
