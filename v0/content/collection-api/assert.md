---
title: "assert"
weight: 91
---

Raises [assert_err()](../../errors/assert_err) if the specified statement evaluates to `false`.

This function does *not* generate an [event](../../overview/events).

### Function

`assert(statement [, error_msg])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
statement | any (required) | The statement to evaluate.
msg | str (optional) | Custom error message.

### Return value

Assert returns with the return value of the given statement when the statement evaluates to `true`. Otherwise
an [assert_err()](../../errors/assert_err) is raised.

### Example

> This code shows how assert can be used:

```thingsdb,should_err
assert(1 > 2, 'one is still smaller than two');
```

> Raises an [assert_err()](../../errors/assert_err) exception

```json
{
    "error_msg": "one is still smaller than two",
    "error_code": -50
}
```
