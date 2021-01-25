---
title: "filter"
weight: 87
---

The function returns a new set with things that pass the test.

This function does *not* generate an [event](../../../overview/events).

### Function

*set*.`filter(callback)`

### Arguments

| Argument | Type               | Description                       |
| -------- | ------------------ | --------------------------------- |
| callback | closure (required) | Closure to execute on each value. |

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
set      | thing, id   | Iterate over things in the set. Both `thing` and `id` are optional.

### Return value

A new `set` with the things that pass the test.
If no items passed the test, an empty set will be returned.

### Example

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
