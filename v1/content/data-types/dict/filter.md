---
title: "filter"
weight: 65
---

The function returns a new dict with key/value pairs that pass the test.

This function does *not* generate a [change](../../../overview/changes).

### Function

*thing*.`filter(callback)`

### Arguments

| Argument | Type               | Description                       |
| -------- | ------------------ | --------------------------------- |
| callback | closure (required) | Closure to execute on each key/value pair. |

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
dict     | key, value  | Iterate over the key/value pairs. Both `key` and `value` are optional.

### Return value

A new `dict` with the key/value pairs that pass the test.
If no pairs pass the test, a empty dict will be returned.

### Example

> This code shows an example using ***filter()***:

```thingsdb,json_response
d = dict([
    [1, "pass"],
    [2, "fail"],
    [3, "fail"],
]);

/*
 * Return a dict where the value is equal to 'fail'
 */

d.filter(|_, v| v == 'fail');
```

> Return value in JSON format (Warning: the order is *NOT* guaranteed)

```json
[
    [2, "fail"],
    [3, "fail"]
]
```
