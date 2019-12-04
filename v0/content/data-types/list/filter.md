---
title: "filter"
weight: 34
---

When this method is used on an [list](..) or [tuple](../../tuple), a new list is returned with elements that pass the test.

This function does *not* generate an [event](../../../overview/events).

### Function

*array*.`filter(callback)`

### Arguments

The *callback* argument must be a `closure` which input values depend on the type the method is called on.

Iterable | Arguments   | Description
-------- | ----------- | -----------
array    | item, index | Iterate over all items in the array. Both `item` and `index` are optional.

### Return value

A new `list` with the elements that pass the test.
If no elements pass the test, an empty list will be returned.

### Example

> This code shows an example using ***filter()***:

```thingsdb,json_response
users = [{name: 'Iris', age: 6}, {name: 'Sasha', age: 34}];

/*
 * Return all users with age 18 or above
 */

users.filter(|user| user.age >= 18);
```

> Return value in JSON format

```json
[
    {
        "age": 34,
        "name": "Sasha"
    }
]
```
