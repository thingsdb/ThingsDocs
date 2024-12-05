---
title: "filter"
weight: 79
---

The function returns a new list with items that pass the test.

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`filter(callback)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure (required) | Closure to execute on each value.

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
array    | item, index | Iterate over all items in the array. Both `item` and `index` are optional.

### Return value

A new `list` with the items that pass the test.
If no items passed the test, an empty list will be returned.

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
