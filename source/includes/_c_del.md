## del

> This code shows some return values for ***del()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        x = 'create and delete this prop';
        del('x');
    ''', scope='@:stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q << EOQ "
x = 'create and delete this prop';
del('x');
"
EOQ
```

> Return value in JSON format

```json
null
```

Delete a property from a [thing](#thing-type).

This function generates an [event](#events).

### Function
*thing*.`del(property)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
property | raw (required) | Name of the property to delete.

### Return value
Returns `nil` if successful. An `INDEX_ERROR` is returned
if the property does not exist or `BAD_REQUEST` in case the given property is
not a valid [name](#names).
