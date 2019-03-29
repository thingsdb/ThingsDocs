## try

> This code shows some return values for ***try()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        try( (1/0) );
        try( (1/0), 0 );
        try( (1/0), 0, 'ZERO_DIV_ERROR' );
        try( (1/0), 0, 97 );
    ''', target='stuff', all=True)
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -a -q << EOQ "
try( (1/0) );
try( (1/0), 0 );
try( (1/0), 0, 'ZERO_DIV_ERROR' );
try( (1/0), 0, 97 );
"
EOQ
```

> Return value in JSON format

```json
[
    null,
    0,
    0,
    0
]
```

Try a statement and if the statement fails with an error, then `nil` is returned unless
an alternative return value is specified. It is also possible to *catch* only specific
[errors](#errors).

<aside class="warning">
It is possible to catch all errors with the exception of <code>INTERNAL_ERROR</code>.
Such error should never happen, unless something is really wrong with at least one node.
</aside>

This function does *not* generate an [event](#events).

### Function
`try(statement, [alt, [e0, e1, ..., eX]])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
statement | any (required) | The statement to try.
alt | any (optional) | Alternative value which is returned if the statement has failed.
e0, e1, ..., eX | int/raw (optional) | Only catch specific errors, if omitted, catch all errors. Error codes and names are accepted.

<aside class="notice">
The <code>alt</code> argument will be <i>lazy</i> evaluated. Consider the following example:
<p><code>try( (1/x), items.pop(), "ZERO_DIV_ERROR");</code></p>
In this example, the item will only be popped in case <code>x</code> is equal to <code>0</code>.
</aside>

### Return value
The value for the specified *statement* unless the statement has failed.