## t
> This code shows an example usage of ***t()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        t(7);
        t(8,);
        t(7, 8);
    ''',target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
t(7);
t(8,);
t(7, 8);
"
EOQ
```

> Return value in JSON format

```json
[
    {
        "#": 7,
        "greet": "Hello"
    },
    [
        {
            "#": 8,
            "to": "world!!"
        }
    ],
    [
        {
            "#": 7,
            "greet": "Hello"
        },
        {
            "#": 8,
            "to": "world!!"
        }
    ]
]
```

This function can be used to get a thing or multiple things by id.

This function is limited to the [collection](#collection-api) scope.

This function does *not* generate an [event](#events).

### Function
`t(id1, id2, ..., idX)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
id1, id2, ..., idX | int (at least one required) | The thing(s) to return.

### Return value
Returns a [thing ](#thing) or an *array-of-things* based on given id's.
An `INDEX_ERROR` is returned in case at least one id is not found inside the collection.

<aside class="notice">
You can force an <i>array</i>, even with only one id. Just add an extra comma,
for example: <code>thing(666,);</code> and this will return an array with one thing: <code>[{"#": 666, ...}]</code>
</aside>
