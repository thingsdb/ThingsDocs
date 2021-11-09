---
title: "args"
weight: 125
---

Get task arguments as a new list.
As this function returns a new list, making changes to this list does *not* affect the task arguments.

This function does *not* generate a [change](../../../overview/changes).

### Function

*task*.`args()`

### Arguments

None

### Return value

Returns a new `list` with arguments.

### Example

> This code will will be called every minute for 10 times and then the task will be removed.

```thingsdb,json_response
t = task(
    datetime().move('days', 1),
    |task, a, b| {
        .sum = a + b;
    },
    [4, 6]
);

t.args();  // Return the task arguments
```

> Return value in JSON format

```json
[
    4,
    6
]
```