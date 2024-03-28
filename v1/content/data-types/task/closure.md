---
title: "closure"
weight: 149
---

Get the closure of a task.

This function does *not* generate a [change](../../../overview/changes).

### Function

*task*.`closure()`

### Arguments

None

### Return value

Returns the closure of the task.

### Example

> Example usage ***task.closure()***:

```thingsdb,json_response
t = task(datetime(), ||log('Dummy task'));
t.closure();
```

> Return value in JSON format

```json
"||log('Dummy task')"
```
