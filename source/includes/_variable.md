# Variable

> This code uses a variable:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        $tmp = 'This is a variable!!!';
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
# note that we need to escape the $ sign in bash
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
\$tmp = 'This is a variable!!!';
"
EOQ
```

> Return value in JSON format

```json
"This is a variable!!!"
```

Can be used to assign a value to a variable which can be used within a query.

A variable can be used withing the scope of a query and is automatically
destroyed after the query is finished.

Variable can be created with `READ` privileges since they do not modify
the collection data.

To create a variable, start with a dollar `$` sign, followed with a valid [name](#names).

Some valid examples:

- `$_ = ...`
- `$tmp = ...`
- `$var1 = ...`

<aside class="notice">
It is possible to re-assign or change a variable within a query, as long as the variable
is not in use within the statement, for example:
<p><code>$tmp = [1, 2]; $tmp.map(|| $tmp = nil);</code></p>
<p>...will raise a <code>BAD_REQUEST</code> <i>(cannot assign a new value to `$tmp` while the variable is in use)</i></p>
</aside>
