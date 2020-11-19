---
title: "each"
weight: 72
---

Iterate over items in a [set](..).

{{% notice warning %}}
Be aware that the order when iterating over a *set* or a *thing* is not guaranteed.
{{% /notice %}}

This function does *not* generate an [event](../../../overview/events).

### Function

*set*.`each(callback)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure (required) | Closure to execute on each value.

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
set      | thing, id   | Iterate over things in the set. Both `thing` and `id` are optional.

### Return value

None

### Example

> This code shows an example using ***each()***:

```thingsdb,json_response
users = set(
    {name: "Iris", age: 6},
    {name: "Sasha", age: 34}
);

// Just an example, the same could be achieved using `filter` and `map`.
old_enough = [];
users.each(|user| user.age >= 18 && old_enough.push(user.name));

// Return all the names of user which are old enough:
old_enough;
```

> Return value in JSON format

```json
[
    "Sasha"
]
```
