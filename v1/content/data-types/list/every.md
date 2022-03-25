---
title: "every"
weight: 66
---

This function checks if all items in the  [list](..) or [tuple](../../tuple) pass a given test. It returns a [boolean](../../bool) value.

{{% notice info %}}
Calling this function on an empty array returns `true` for any condition!
{{% /notice %}}

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`every(callback)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure | Closure to execute on each value until the closure evaluates to false.

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
array    | item, index | Iterate over items in the array. Both `item` and `index` are optional.

### Return value

Returns `true` if every item in the array satisfies the check in the callback function. Otherwise, `false`.

### Example

> This code shows an example using ***every()***:

```thingsdb,json_response
a = [12, 5, 8, 130, 44].every(|x| x >= 10);   // false
b = [12, 54, 18, 130, 44].every(|x| x >= 10); // true

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
