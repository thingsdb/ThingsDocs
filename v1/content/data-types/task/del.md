---
title: "del"
weight: 150
---

Delete a task. After calling this function, the task will be removed from ThingsDB. If there are references to this task, then those references will no longer contain the original task but an empty task instead.

This function generates a [change](../../../overview/changes).

### Function

*task*.`del()`

### Arguments

None

### Return value

Returns `nil`.

### Example

> Example usage ***task.del()***:

```thingsdb,json_response
t = task(datetime(), ||log('Dummy task'));
t.del();  // delete the task before it can start
```

> Return value in JSON format

```json
null
```
