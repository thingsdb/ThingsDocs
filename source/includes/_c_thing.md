## thing
> This code shows an example usage of ***thing()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        .greet = "Hello world!";
        [
            thing(.id()),
            thing(),
        ];
    ''',target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ '
.greet = "Hello world!";
[
    thing(.id()),
    thing(),
];
'
EOQ
```

> Return value in JSON format

```json
[
    {
        "#": 42,
        "greet": "Hello world!"
    },
    {}
]
```

Returns a [thing](#thing-type) from a specified value.
If no value is given, a new thing is returned.

This function does *not* generate an [event](#events).

### Function
`thing([id])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
id | int (optional) | The id for the thing to return.

### Return value
Returns a [thing ](#thing-type).
An `INDEX_ERROR` is returned in case an id is given which is not found inside the collection.
