---
title: "set_closure"
weight: 140
---

Change the closure to execute. Obsolete closure arguments will be removed when the new closure accepts less arguments than the previous closure.
If the new closure accepts more arguments, the argument list will be extended with `nil` values.

This function generates a [change](../../../overview/changes).

### Function

*task*.`set_closure(code)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
code | closure (required) | New closure to attach to the task.

### Return value

Returns `nil` when successful.

### Example

> This code will change the closure of a task.

```thingsdb,should_pass
t = task(datetime(), ||nil);

// Change the closure of the task
t.set_closure(|| {
    log('New closure!');
});
```