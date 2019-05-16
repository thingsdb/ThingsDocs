## filter

> This code shows an example using ***filter()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        /* Return all users with age 18 or above */
        users.filter(|user| (user.age >= 18));

        /* Return a `thing` with only property `age` */
        users[0].filter(|prop| (prop == 'age'));
    ''', target='stuff', deep=2, all_=True)
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -d 2 -a -q << EOQ "
/* Return all users with age 18 or above */
users.filter(|user| (user.age >= 18));

/* Return a thing with only property age */
users[0].filter(|prop| (prop == 'age'));
"
EOQ
```

> Example return value in JSON format

```json
[
    [
        {
            "#": 3,
            "age": 34,
            "name": "Sasha"
        },
        {
            "#": 4,
            "age": 40,
            "name": "Jeroen"
        }
    ],
    {
        "#": 0,
        "age": 34
    }
]
```


If this method is used on a `thing`, then a new thing will be returned with only
the properties that pass the test. If the method is used on an `array`, then a
new array is returned with elements that pass the test.

This function does *not* generate an [event](#events).

### Function
*iterable*.`filter(callback)`

### Arguments
The *callback* argument must be a `closure` which input values depend on the type the method is called on.

Iterable | Arguments | Description
-------- | -------- | -----------
array | item, index | Iterate over all items in the array. Both item and index are optional.
thing | name, value | Iterate over the thing properties. Both name and value are optional.


### Return value
A new `array` or `thing` with the elements or properties that pass the test.
If no elements or properties pass the test, an empty array or thing will be returned.
