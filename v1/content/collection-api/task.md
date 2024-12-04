---
title: "task"
weight: 311
---

Create a new task or get an existing task by Id.

Using an Id as a single argument, this function can be used to return an existing task. With [tasks()](../tasks) you can get a list with all available tasks.

This function generates a [change](../../overview/changes).

### Function

`task(Id)` *(get a task by Id)*
`task(start, code, [args])` *(create a new task)*

### Arguments

Argument | Type | Description
-------- | ---- | -----------
Id       | int (required) | The Id of the task to return.

Argument | Type | Description
-------- | ---- | -----------
start | datetime (required) | Date/time to execute the task.
code | closure (required) | Closure to execute at the scheduled date/time.
args | list (optional) | Optional list with task arguments.

### Return value

A new task or existing task if called with an `Id`.

### Example

> The following code creates a one-time task:

```thingsdb,should_pass
start = datetime().move('minutes', 1);

task(start, || {
    log('One time task!');
});
```

> The code below is an example of a repeating task:

```thingsdb,should_pass
start = datetime().move('days', 1).replace({
    hour: 20,
    minute: 0,
    second: 0
});

task(start, |task| {
    task.again_in('days', 7);
    log('Weekly task');
});
```
