---
title: "assert"
weight: 123
---

Raises an [assert_err()](../../errors/assert_err) if the specified expression evaluates to `false`.

This function does *not* generate an [event](../../overview/events).

### Function

`assert(expression [, error_msg])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
expression | any (required) | The expression to evaluate.
error_msg | str (optional) | Custom error message.

### Return value

Returns `nil` if the type of the expression evaluates to `true`. Otherwise
an [assert_err()](../../errors/assert_err) is raised.

{{% notice warning %}}
In versions before **v0.9.4** the return value of `assert(..)` used to be the return value from the expression *(when evaluated as `true`)*.
{{% /notice %}}

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
