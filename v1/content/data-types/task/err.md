---
title: "err"
weight: 134
---

When a task as failed with an error, the error is stored on the task and the task will not be removed automatically.
With this function you may get the error to view and/or debug the problem.

This function does *not* generate a [change](../../../overview/changes).

### Function

*task*.`err()`

### Arguments

None

### Return value

Returns the error when a task has failed or `nil` if the task is empty or without error.

### Example

> Example usage ***task.err()***:

```thingsdb,should_pass
.my_task = task(datetime(), || 1/0);
```

Suppose we wait a few seconds and then check the task for errors:

```thingsdb,syntax_only
.my_task.err()
```

> Return value in JSON format

```json
"division or modulo by zero"
```
