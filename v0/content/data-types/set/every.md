---
title: "every"
weight: 93
---

This function checks if all things in the [set](..) pass a given test. It returns a [boolean](../../bool) value.

{{% notice info %}}
Calling this function on an empty set returns `true` for any condition!
{{% /notice %}}

This function does *not* generate an [event](../../../overview/events).

### Function

*set*.`every(callback)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure | Closure to execute on each thing until the closure evaluates to false.

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
set      | thing, Id | Iterate over things in the set. Both `thing` and `id` are optional.

### Return value

Returns `true` if every thing in the set satisfies the check in the callback function. Otherwise, `false`.

### Example

> This code shows an example using ***every()***:

```thingsdb,json_response
users = set({
    name: 'Iris',
    age: 7,
}, {
    name: 'Tess',
    age: 6
});

a = users.every(|user| user.age > 6);  // false
b = users.every(|user| user.age > 3);  // true

// Return both a and b
[a, b];
```

> Return value in JSON format

```json
[
    false,
    true
]
```
