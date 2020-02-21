---
title: "some"
weight: 49
---

This function tests whether at least one element in the array passes a given test. It returns a [boolean](../../bool) value.

{{% notice info %}}
Calling this function on an empty array returns `false` for any condition!
{{% /notice %}}

This function does *not* generate an [event](../../../overview/events).

### Function

*array*.`some(callback)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure | Closure to execute on each value until the closure evaluates to true.

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
array    | item, index | Iterate over items in the array. Both `item` and `index` are optional.

### Return value

Returns `true` if the callback function returns a *truthy* value for at least one element in the array. Otherwise, `false`.

### Example

> This code shows an example using ***find()***:

```thingsdb,json_response
a = [2, 5, 8, 1, 4].some(|x| x >= 10);   // false
b = [12, 5, 8, 1, 4].some(|x| x >= 10);  // true

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