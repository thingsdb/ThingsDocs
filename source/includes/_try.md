## try

> This code shows some return values for ***try()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        try( (1/0) );
        try( (1/0), 0 );
        try( (1/0), 0, ZERO_DIV_ERROR );
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
try( (1/0) );
try( (1/0), 0 );
try( (1/0), 0, ZERO_DIV_ERROR );
"
EOQ
```

> Return value in JSON format

```json
[
    null,
    0,
    0
]
```

Try a statement and if the statement fails with an error, then `nil` is returned unless
an alternative return value is specified. It is also possible to *catch* only specific
[errors](#errors).

This function does *not* generate an [event](#events).

### Function
`try(statement, [alt, [e0, e1, ..., eX]])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
statement | any (required) | The statement to try.
alt | any (optional) | Alternative value which is returned if the statement has failed.
e0, e1, ..., eX | int (optional) | Only catch specific errors, if omitted, catch all errors.

### Return value
The value for the specified *statement* unless the statement has failed.