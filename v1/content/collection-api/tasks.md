---
title: "tasks"
weight: 265
---

Return a list with all the tasks in the current scope.

This function does *not* generate a [change](../../overview/changes).

### Function

`tasks()`

### Arguments

None

### Return value

A list with all the tasks in the current scope.

### Example

> Example ***tasks()***:

```thingsdb,should_pass
tasks();
```

> Example return value in JSON format

```json
[
    "<task:9 owner:admin run_at:nil status:err>",
    "<task:10 owner:admin run_at:2021-11-03T12:43:57Z status:nil>",
    "<task:26 owner:admin run_at:2021-11-03T20:00:00Z status:nil>"
]
```

> Example how to use ***tasks()*** to get all task Ids:

```thingsdb,should_pass
tasks().map(|t| t.id());
```

> Example return value in JSON format

```json
[
    9,
    10,
    26
]
```