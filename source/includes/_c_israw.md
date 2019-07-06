## israw

> This code shows some return values for ***israw()***:

```python
import asyncio
import urllib
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    client.authenticate(auth=['admin', 'pass'])

    # TODO: replace with ThingsDB logo
    resp = urllib.request.urlopen(
        'https://upload.wikimedia.org/wikipedia/commons/1/15/Siridb-logo.svg')

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
wget -O - 'https://upload.wikimedia.org/wikipedia/commons/1/15/Siridb-logo.svg' | \
thingscmd -n node.local -u admin -p pass -c stuff -q  << EOQ "
[
    israw( 'some string' ),
    israw( blob(0) ),
];
"
EOQ
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
