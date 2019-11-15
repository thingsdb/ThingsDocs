---
title: "err"
date: 2019-10-14T09:58:22+02:00
weight: 600
---

Returns an [error](../../data-types/error).

This function does *not* generate an [event](../../events).

### Function

`err([code, [message]])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
code | int (optional) | Integer error code between -127 and -50, defaults to -100.
message | str (optional) | Optional error message.

### Return value

An error value.

> This code shows some return values for ***err()***:

```thingsdb,json_response
[
    err(),
    err(-100, 'some error occurred'),
    err(-101),
    err(-59),
];
```

> Return value in JSON format

```json
[
    {
        "!": "err(-100)",
        "error_code": -100,
        "error_msg": "error:-100"
    },
    {
        "!": "err(-100)",
        "error_code": -100,
        "error_msg": "some error occurred"
    },
    {
        "!": "err(-101)",
        "error_code": -101,
        "error_msg": "error:-101"
    },
    {
        "!": "overflow_err()",
        "error_code": -59,
        "error_msg": "integer overflow"
    }
]
```
