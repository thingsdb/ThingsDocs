## filter

> This code shows an example using ***filter()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        users = [{name: 'Iris', age: 6}, {name: 'Sasha', age: 34}];

        /*
         * Return all users with age 18 or above and
         * a `thing` with only property `age`
         */

        [
            users.filter(|user| (user.age >= 18)),
            users[0].filter(|prop| (prop == 'age')),
            set(users).filter(|user| (user.name == 'Iris')),
        ];
        => 3
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
users = [{name: 'Iris', age: 6}, {name: 'Sasha', age: 34}];

/*
 * Return all users with age 18 or above,
 * a thing with only property age,
 * and all users with name 'Iris'.
 */

[
    users.filter(|user| (user.age >= 18)),
    users[0].filter(|prop| (prop == 'age')),
    set(users).filter(|user| (user.name == 'Iris')),
];
=> 3
"
EOQ
```

> Return value in JSON format

```json
[
    [
        {
            "#": 0,
            "age": 34,
            "name": "Sasha"
        }
    ],
    {
        "#": 0,
        "age": 6
    },
    [
        {
            "#": 0,
            "age": 6,
            "name": "Iris"
        }
    ]
]
```


If this method is used on a `thing`, then a new thing will be returned with only
the properties that pass the test. If the method is used on an `array`, then a
new array is returned with elements that pass the test and if used on a `set`, then
the return value will be a new set.

This function does *not* generate an [event](#events).

### Function
*iterable*.`filter(callback)`

### Arguments
The *callback* argument must be a `closure` which input values depend on the type the method is called on.

Iterable | Arguments   | Description
-------- | ----------- | -----------
array    | item, index | Iterate over all items in the array. Both `item` and `index` are optional.
set      | thing, id   | Iterate over things in the set. Both `thing` and `id` are optional.
thing    | name, value | Iterate over the thing properties. Both `name` and `value` are optional.


### Return value
A new `array`, `set` or `thing` with the elements or properties that pass the test.
If no elements or properties pass the test, an empty array, set or thing will be returned.
