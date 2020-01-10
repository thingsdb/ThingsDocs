---
title: "str"
weight: 134
---

Convert a value to a string. If no value is given, an empty string `""` is returned.

When [bytes](../../data-types/bytes) are converted to [str](../../data-types/str) then the data will be checked
if it contains valid UTF-8 characters. If this is not the case, a `VALUE_ERROR` will be raised.

This function does *not* generate an [event](../../overview/events).

### Function

`str(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (optional) | The value to create a string from.

### Return value

A new string

### Example

> This code shows some return values for ***str()***:

```thingsdb,json_response
[
    str(),
    str(42),
    str(true)
];
```

> Return value in JSON format

```json
[
    "",
    "42",
    "true"
]
```