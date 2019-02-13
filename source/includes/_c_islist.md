## islist

> This code shows some return values for ***islist()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        islist( [] );
        islist( {} );
        islist( [1, 'two', 3.0] );
        islist( [{some: 'array'}, {with: 'things'}] );
        islist( [['nested', 'therefore this is a tuple']][0] );
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
islist( [] );
islist( {} );
islist( [1, 'two', 3.0] );
islist( [{some: 'array'}, {with: 'things'}] );
islist( [['nested', 'therefore this is a tuple']][0] );
"
EOQ
```

> Return value in JSON format

```json
[
    true,
    false,
    true,
    false,
    false
]
```

This function determines whether the value passed to this function
is a list type or not.

This function does *not* generate an [event](#events).

### Function
`islist(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested for being a list.

### Return value
Returns `true` the value passed is list else it returns `false`.

<aside class="notice">
The <code>islist()</code> function returns <code>true</code> for an empty, not-nested, <i>array-of-things</i> because it will
take any value and therefore can convert to a list.
</aside>
