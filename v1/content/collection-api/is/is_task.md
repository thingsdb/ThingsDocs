---
title: "is_task"
weight: 250
---

This function determines whether the provided value is a [task](../../../data-types/task) or not.

This function does *not* generate a [change](../../../overview/changes).

### Function

`is_task(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is a `task`, else it returns `false`.

### Example

> This code shows some return values for ***is_task()***:

```thingsdb,json_response
[
    is_task( thing() ),
    is_task( task(datetime(), ||nil) ),
];
```

> Return value in JSON format

```json
[
    false,
    true
]
```
