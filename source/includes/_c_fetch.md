## fetch

> This code shows how to use ***fetch()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        users.fetch();
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
users.fetch();
"
EOQ
```

> Example return value in JSON format

```json
[

]
```

The default behavior when returning an array-of-things is to return only the id's, and no other properties.
When calling function `fetch()` the things are returned including their properties.

<aside class="warning">
Function <code>fetch()</code> can be called on any iterable, but is has only effect on an array-of-things.
</aside>

This function does *not* generate an [event](#events).

### Function
*i`try(statement, [alt, [e0, e1, ..., eX]])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
statement | any (required) | The statement to try.
alt | any (optional) | Alternative value which is returned if the statement has failed.
e0, e1, ..., eX | int/raw (optional) | Only catch specific errors, if omitted, catch all errors. Error codes and names are accepted.

### Return value
The value for the specified *statement* unless the statement has failed.