---
title: "id"
weight: 149
---

Returns the `id` of a [task](..) or `nil` if the task is removed *(empty)*.

Notice that *every* task will be stored, thus all new tasks will get an Id. Only when a task is *successfully* finished or removed using [del()](../del), the task will be empty and therefore the Id will be `nil`.

This function does *not* generate a [change](../../../overview/changes).

### Function

*task*.`id()`

### Arguments

None

### Return value

Returns `id` of a task or `nil` if the task is removed *(empty)*.

### Example

> This code uses `id()` to return a task id:

```thingsdb,should_pass
t = task(datetime().move('days', 1), ||log('Dummy task'));
t.id();  // Returns the Id of the task.
```

> Example return value in JSON format

```json
624
```
