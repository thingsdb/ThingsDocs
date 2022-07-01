---
title: "range"
weight: 257
---

This function returns a [list](../../data-types/list) of numbers, starting from 0 (by default), increments by 1 (by default), and ends at a specified number.

{{% notice warning %}}
Function **range()** may only be used for relatively small lists.
An [operation_err()](../../errors/operation_err) *(maximum range length exceeded)* will be raised when trying to create a list with more than **1024** numbers.
{{% /notice %}}

### Function

`range(start, stop, step)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`start` | int (optional) | An integer number specifying at which position to start. Default is `0`
`stop` | int (required) | An integer number specifying at which position to end (*exclusive*).
`step` | int (optional) | An integer number specifying the increment value. Default is `1` and this value must not be zero.

### Return value

Returns a [list](../../data-types/list) of numbers.

### Examples

> Return a list with numbers `0` to `5`:

```thingsdb,json_response
range(6);
```

```json
[0, 1, 2, 3, 4, 5]
```

> Return a list with numbers `0` to `5` but increment by `2`:

```thingsdb,json_response
range(0, 6, 2);
```

```json
[0, 2, 4]
```

> The `step` argument may also be a negative value:

```thingsdb,json_response
range(2, -3, -1);
```

```json
[2, 1, 0, -1, -2]
```
