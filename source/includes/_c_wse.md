## wse

> This code shows an example usage for ***wse()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        wse({
            x = 0;
            a = |v| x += v;
            [1 ,2 ,3, 4].map(a);  /* without wse() this would raise an error */
            x;
        });
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
wse({
    x = 0;
    a = |v| x += v;
    [1 ,2 ,3, 4].map(a);  /* without wse() this would raise an error */
    x;
});
"
EOQ
```

> Return value in JSON format

```json
10
```

Stored closures which can potentially make changes to ThingsDB are called
*closures with side effects* and must be wrapped with the `wse(..)` function.

This allows ThingsDB to know ahead for running the query to make an event.
You should not wrap `wse` around all closures since this would unnecessary
create events when they may not be required.

This function generates an [event](#events).

### Function
`wse(statement)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
statement | any | Statement or block to wrap.

### Return value
Return value of the given statement.
