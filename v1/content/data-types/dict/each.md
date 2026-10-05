---
title: "each"
weight: 64
---

Iterate over items in a [dict](..).

{{% notice warning %}}
Be aware that the order when iterating over a *dict*, *dict* or a *thing* is not guaranteed.
{{% /notice %}}

This function does *not* generate a [change](../../../overview/changes).

### Function

*dict*.`each(callback)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure (required) | Closure to execute on each value.

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
dict      | key, value | Iterate over items in the dict. Both `key` and `value` are optional.

### Return value

None

### Example

> This code shows an example using ***each()***:

```thingsdb,json_response
users = dict([
    [uuid(), {name: "Iris", age: 6}],
    [uuid(), {name: "Sasha", age: 34}],
]);

// Just an example, the same could be achieved using `filter` and `map`.
old_enough = [];
users.each(|_, user| user.age >= 18 && old_enough.push(user.name));

// Return all the names of user which are old enough:
old_enough;
```

> Return value in JSON format

```json
[
    "Sasha"
]
```
