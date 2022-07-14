---
title: "cancel"
weight: 136
---

Cancel a task. Using this function sets the task error to *[cancelled_err](../../../errors//cancelled_err)* and the task will not be executed. This function differs from [del()](../del) as it will not remove the task.

This function generates a [change](../../../overview/changes).

### Function

*task*.`cancel()`

### Arguments

None

### Return value

Returns `nil`.

### Example

> Example usage ***task.cancel()***:

```thingsdb,json_response
t = task(datetime(), ||log('Dummy task'));
t.cancel();  // cancel the task before it can start
```

> Return value in JSON format

```json
null
```
