# Variable

> This code uses a variable:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        a = 'This is a variable!!!';
        b = 'Hello';
        {
            /* This will create a new variable `a` within this scope */
            a = 'New variable within this block';

            /* This will update the global variable `b` */
            b += ' World';
        };
        [a, b];
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
a = 'This is a variable!!!';
b = 'Hello';
{
    /* This will create a new variable `a` within this scope */
    a = 'New variable within this block';

    /* This will update the global variable `b` */
    b += ' World';
};
[a, b];
"
EOQ
```

> Return value in JSON format

```json
[
    "This is a variable!!!",
    "Hello World"
]
```

Can be used to assign a value to a variable which can be used within a query.

Variable can be created with `READ` privileges since they do not modify
the collection data.

To create a variable, just use a valid [name](#names).

Some valid examples:

- `_ = ...`
- `tmp = ...`
- `var1 = ...`

