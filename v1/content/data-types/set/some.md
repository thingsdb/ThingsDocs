---
title: "some"
weight: 139
---

This function checks if at least one thing in the [set](..) passes a given test. It returns a [boolean](../../bool) value.

{{% notice info %}}
Calling this function on an empty set returns `false` for any condition!
{{% /notice %}}

This function does *not* generate a [change](../../../overview/changes).

### Function

*set*.`some(callback)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure | Closure to execute on each thing until the closure evaluates to true.

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
set      | thing, Id | Iterate over things in the set. Both `thing` and `id` are optional.

### Return value

Returns `true` if at least one thing in the set satisfies the check in the callback function. Otherwise, `false`.

### Example

> This code shows an example using ***some()***:

```thingsdb,json_response
users = set({
    name: 'Iris',
    age: 7,
}, {
    name: 'Tess',
    age: 6
});

a = users.some(|user| user.age > 18); // false
b = users.some(|user| user.age > 6);  // true

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
