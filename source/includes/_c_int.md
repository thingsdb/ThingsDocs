## int

> This code shows some return values for ***int()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        int(2.718);
        int(-1.9);
        int('365 days');
        int('0xFF');
        int(true);
        int(false);
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
int(2.718);
int(-1.9);
int('365 days');
int('0xFF');
int(true);
int(false);
"
EOQ
```

> Return value in JSON format

```json
[
    2,
    -1,
    365,
    255,
    1,
    0
]
```

Returns an [int](#integer) from a specified value.

If the specified value was a [float](#floating-point) value, then the
new integer value will be rounded towards zero.

If the specified value is of type [raw](#string-raw), then the initial characters
of the string are converted until a non-digit character is found.
Initial white space is ignored and the number may start with an optional `+` or `-` sign.

Type [bool](#boolean) values are converted to `1` for `true` and `0` for `false`.

This function does *not* generate an [event](#events).

### Function
`int(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value where to create an integer value for.

### Return value
An integer value. In case the integer value is too large for a 64bit integer,
an `OVERFLOW_ERROR` is raised. Other type than `float`, `raw`, `bool` or `int`
will raise a `BAD_REQUEST`.
