## iserr

> This code shows some return values for ***iserr()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        [
            iserr( err() ),
            iserr( zero_div_err() ),
            iserr( try((1 / 0)) ),
            iserr( try((1 / 1)) ),
        ];
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
[
    iserr( err() ),
    iserr( zero_div_err() ),
    iserr( try((1 / 0)) ),
    iserr( try((1 / 1)) ),
];
"
EOQ
```

> Return value in JSON format

```json
[
    true,
    true,
    true,
    false
]
```

This function determines whether the value passed to this function
is a [error](#error-type) or not.

This function does *not* generate an [event](#events).

### Function
`iserr(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value
Returns `true` is the passed value is an error else it returns `false`.