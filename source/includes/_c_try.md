## try

> This code shows some return values for ***try()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        [
            iserr( try( x = (1/0) )),
            iserr( try( (1/0), zero_div_err() )),
        ];
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ '
[
    iserr( try( x = (1/0) )),
    iserr( try( (1/0), zero_div_err() )),
];
'
EOQ
```

> Return value in JSON format

```json
[
    true,
    true
]
```

Try a statement and if the statement fails with an error, then the error is returned.
It is also possible to *catch* only specific [errors](#errors).

<aside class="warning">
It is possible to catch all errors with the exception of *internal errors*.
Such errors should never happen, unless something is really wrong with at least one node.
</aside>

This function does *not* generate an [event](#events).

### Function
`try(statement, [e0, e1, ..., eX])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
statement | any (required) | The statement to try.
e0, e1, ..., eX | int/raw (optional) | Only catch specific errors, if omitted, catch all errors. Error codes and names are accepted.

### Return value
The value for the specified *statement* or an error if the statement has failed.