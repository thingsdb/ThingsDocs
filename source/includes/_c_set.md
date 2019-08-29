## set (new-type)

> This code shows some return values for ***set()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        set({}, {});
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
set({}, {});
"
EOQ
```

> Return value in JSON format

```json
{
    "$": [
        {
            "#": 0
        },
        {
            "#": 0
        }
    ]
}
```

Returns a new empty [set](#set-type). If an array is given, then all elements in the
given array must be or type `thing` and a new set is returned based on the
given things. Instead of an array, it is also possible to provide things comma separated.

<aside class="warning">
When creating a new set with a single thing, make sure to add a comma <code>set({},)</code>  to enforce an array, or actually wrap the thing in an array <code>set( [{}] )</code>.
</aside>

This function does *not* generate an [event](#events).

### Function
`set([array])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
array | array (optional) | Optional array to initialize the set.

### Return value
A new set.

## set (property)

> This code shows how to use ***set()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        .set('the_answer', 42);
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
.set('the_answer', 42);
"
EOQ
```

> Return value in JSON format

```json
42
```

Creates a new property on a thing. If the property already existed then the old
property will be overwritten. This function is equal to an assignment except that
it can be used when the `name` of the property is dynamic.

This function generates an [event](#events).

### Function
*thing*.`set(name, value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
name | raw (required) | The name of the property to set.
value | any (required)  | The value which will be assigned to the property.

### Return value
The value which will be assigned.
