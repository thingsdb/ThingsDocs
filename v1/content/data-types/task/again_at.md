---
title: "again_at"
weight: 139
---

Re-schedules the task to a new date/time. The task will run again at the new date/time, even if the task returns with an error.

{{% notice note %}}
It is only possible to use `again_at` within the callback of the parent task. If may however be used within a future or other closure, as long as this closure is nested within the tasks callback.
{{% /notice %}}

This function generates a [change](../../../overview/changes).

### Function

*task*.`again_at(start)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`start` | `datetime` (required) | Date/time when the task should start again.

### Return value

Returns `nil` when successful.

### Example

> This code creates a repeating task:

```thingsdb,should_pass
start = datetime();

// Create a repeating task (daily at 23:00)
task(start, |task| {
    // Run the task again in one day, relative to the current time.
    // tip: use again_in() to move the task relative to the task scheduled time.
    task.again_at(datetime().move('days', 1));
    log('Daily task');
});
```

> Example return value in JSON format

```json
"<task:12 owner:admin run_at:2021-11-02T13:05:11Z status:nil>"
```