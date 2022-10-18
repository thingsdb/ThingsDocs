---
title: "type_assert"
weight: 284
---

Raises a [type_err()](../../errors/type_err) if the specified expression evaluates to `false`.

This function does *not* generate a [change](../../overview/changes).

### Function

`assert(expression, type(s) [, error_msg])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
expression | any (required) | The result of this expression will be *type tested*.
type(s) | str/list (required) | Type name *or* list with type names to check.
error_msg | str (optional) | Custom error message.

### Return value

Returns `nil` if the type of the expression evaluates to `true`. Otherwise
an [type_err()](../../errors/type_err) is raised.

### Example

> This code shows how assert can be used:

```thingsdb,should_err
type_assert("one", "int");
```

> Raises a [type_err()](../../errors/type_err) exception

```json
{
    "error_msg": "invalid type `str`",
    "error_code": -61
}
```

Or, use a `list` of type names to check

```thingsdb,json_response
type_assert(3.14, ["int", "float"]);
```

> Return value in JSON format

```json
null
```
