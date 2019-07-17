## err

> This code shows some return values for ***err()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        [
            err(),
            err(-100, 'some error occurred'),
            err(-101),
            err(-59),
        ];
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
[
    err(),
    err(-100, 'some error occurred'),
    err(-101),
    err(-59),
];
"
EOQ
```

> Return value in JSON format

```json
[
    {
        "!": "err(-100)",
        "error_code": -100,
        "error_msg": "error:-100"
    },
    {
        "!": "err(-100)",
        "error_code": -100,
        "error_msg": "some error occurred"
    },
    {
        "!": "err(-101)",
        "error_code": -101,
        "error_msg": "error:-101"
    },
    {
        "!": "overflow_err()",
        "error_code": -59,
        "error_msg": "integer overflow"
    }
]
```

Returns an [error](#error-type).

This function does *not* generate an [event](#events).

### Function
`err([code, [message]])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
code | int (optional) | Integer error code between -127 and -50, defaults to -100.
message | raw (optional) | Optional error message.


### Return value
An error value.
