---
title: "err"
weight: 224
---

Returns an [error](../../data-types/error).

This function does *not* generate a [change](../../overview/changes).

### Function

`err([code, [message]])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
code | int (optional) | Integer error code between -127 and -50, defaults to -100. See [error documentation](../../errors) for build-in errors.
message | str (optional) | Optional error message.

### Return value

An error value *(in a client response, an error value will be packed as a string value with the error message)*.

### Example

> This code shows some return values for ***err()***:

```thingsdb,json_response
// Error 59 is the internal integer overflow error
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
    "error:-100",
    "some error occurred",
    "error:-101",
    "integer overflow"
]
```
