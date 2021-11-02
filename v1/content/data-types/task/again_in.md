---
title: "again_in"
weight: 124
---

Re-schedules the task to a new date/time. The task will run again at the new date/time, even if the task returns with an error.

{{% notice note %}}
It is only possible to use `again_at` within the callback of the parent task. If may however be used within a future or other closure, as long as this closure is nested within the tasks callback.
{{% /notice %}}

This function generates a [change](../../../overview/changes).

### Function

*task*.`again_in(unit, num)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`unit` | `str` (required) | One of `years`, `months`, `weeks`, `days`, `hours`, `minutes` or `seconds`.
`num` | `int` (required) | How many times to move the `unit`. A negative number will not work as this would shift the task to run in the past.

### Return value

Returns `nil` when successful.

### Example

> This code create a repeating task:

```thingsdb,should_pass
start = datetime().replace({
    hour: 23,
    minute: 0,
    second: 0,
});

// Create a repeating task (daily at 23:00)
task(start, |task| {
    task.again_in('days', 1);
    log('Daily task');
});
```

> Example return value in JSON format

```json
"<task:13 owner:admin run_at:2021-11-02T23:00:00Z status:nil>"
```