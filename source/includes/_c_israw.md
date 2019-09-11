## israw

> This code shows some return values for ***israw()***:

```python
import asyncio
import urllib
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])

    # TODO: replace with ThingsDB logo
    resp = urllib.request.urlopen(
        'https://thingsdb.github.io/ThingsDocs/images/logo.png')

    res = await client.query(r'''
        [
            israw( 'some string' ),
            israw( blob(0) ),
        ];
    ''', target='stuff', blobs=[resp.read()])
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
wget -O - "https://thingsdb.github.io/ThingsDocs/images/logo.png" |
thingscmd \
    -n node.local \
    -u admin \
    -p pass \
    -c stuff \
    -q " [ israw( 'some string' ), israw( blob(0) ) ]; "
```

> Return value in JSON format

```json
[
    true,
    true
]
```

This function determines whether the value passed to this function is of
type `raw`.

This function does *not* generate an [event](#events).

### Function
`israw(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value
Returns `true` is the given value is of type `raw`, else `false`.
