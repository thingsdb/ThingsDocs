## isarray

> This code shows some return values for ***isarray()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        isarray( [] );
        isarray( {} );
        isarray( [1, 'two', 3.0] );
        isarray( [{some: 'array'}, {with: 'things'}] );
        isarray( [['nested', 'therefore this is a tuple']][0] );
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
isarray( [] );
isarray( {} );
isarray( [1, 'two', 3.0] );
isarray( [{some: 'array'}, {with: 'things'}] );
isarray( [['nested', 'therefore this is a tuple']][0] );
"
EOQ
```

> Return value in JSON format

```json
[
    true,
    false,
    true,
    true,
    true
]
```

This function determines whether the value passed to this function
is an [array](#array) type or not.

This function does *not* generate an [event](#events).

### Function
`isarray(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested for being an array.

### Return value
Returns `true` the value passed is array else it returns `false`.

<aside class="notice">
This function returns <code>true</code> for all array types, <i>list</i>, <i>tuple</i> and <i>array-of-things</i>.
</aside>

