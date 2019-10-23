---
title: "filter"
date: 2019-10-23T12:51:22+02:00
weight: 1
---

If this method is used on a `thing`, then a new thing will be returned with only
the properties that pass the test. If the method is used on an `array`, then a
new array is returned with elements that pass the test and if used on a `set`, then
the return value will be a new set.

This function does *not* generate an [event](../../../events).

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

> This code shows an example using ***filter()***:

```thingsdb,json_response
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
```

> Return value in JSON format

```json
[
    [
        {
            "age": 34,
            "name": "Sasha"
        }
    ],
    {
        "age": 6
    },
    [
        {
            "age": 6,
            "name": "Iris"
        }
    ]
]
```
