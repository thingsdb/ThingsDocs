---
title: "owner"
weight: 152
---

Get the owner of the the task as string value.

This function does *not* generate a [change](../../../overview/changes).

### Function

*task*.`owner()`

### Arguments

None

### Return value

Returns the name of the owner from the task.

### Example

> Example code to get the owner of a task:

```thingsdb,json_response
t = task(datetime(), ||nil);

t.owner();  // Returns the owner of the task
```

> Return value in JSON format

```json
"admin"
```