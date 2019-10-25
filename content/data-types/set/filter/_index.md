---
title: "filter"
date: 2019-10-23T13:52:18+02:00
weight: 2
---

When this method is used on a `set`, then the return value will be a new set.

This function does *not* generate an [event](../../../events).

### Function

*set*.`filter(callback)`

### Arguments

The *callback* argument must be a `closure` which input values depend on the type the method is called on.

Iterable | Arguments   | Description
-------- | ----------- | -----------
set      | thing, id   | Iterate over things in the set. Both `thing` and `id` are optional.

### Return value

A new `set` with the elements that pass the test.
If no elements pass the test, an empty set will be returned.

> This code shows an example using ***filter()***:

```thingsdb,json_response
users = set({name: 'Iris', age: 6}, {name: 'Sasha', age: 34});

/*
 * Return all users with name 'Iris'.
 */

users.filter(|user| (user.name == 'Iris'));
```

> Return value in JSON format

```json
[
    {
        "age": 6,
        "name": "Iris"
    }
]
```
