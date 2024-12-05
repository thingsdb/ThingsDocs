---
title: "at"
weight: 153
---

Get the scheduled start time of a task or `nil` if the task is not scheduled.

This function does *not* generate a [change](../../../overview/changes).

### Function

*task*.`at()`

### Arguments

None

### Return value

Returns the scheduled start time of a task or `nil` if the task is not scheduled.

### Example

> Example usage ***task.at()***:

```thingsdb,json_response
t = task(datetime('2022-01-01'), ||log('Dummy task'));
t.at();
```

> Return value in JSON format

```json
"2022-01-01T00:00:00Z"
```
