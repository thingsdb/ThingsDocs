## has (set)

> This code shows an example use case of ***has()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        iris = {name: 'Iris'};
        set = set([iris]);

        /* Check if iris is in the set */
        set.has(iris);
    ''', scope='@:stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q << EOQ "
iris = {name: 'Iris'};
set = set([iris]);

/* Check if iris is in the set */
set.has(iris);
"
EOQ
```

> Return value in JSON format

```json
true
```

Determines if a [set](#set-type) has a given thing.

This function does *not* generate an [event](#events).

### Function
*set*.`has(thing)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
thing | thing (required) | Thing to check.

### Return value
Returns `true` the given thing is found in the set and otherwise `false`.


## has (thing)

> This code shows an example use case of ***has()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        tmp = {name: 'Iris'};
        tmp.has('name');
    ''', scope='@:stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q << EOQ "
tmp = {name: 'Iris'};
tmp.has('name');
"
EOQ
```

> Return value in JSON format

```json
true
```

Determines if a [thing](#thing-type) has a given property.

This function does *not* generate an [event](#events).

### Function
*thing*.`has(name)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
name | raw (required) | Name of the property to check.

### Return value
Returns `true` when the given propery name is found and otherwise `false`.
