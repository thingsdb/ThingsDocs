---
title: "is_bytes"
weight: 146
---

This function determines whether the provided value is of type [bytes](../../data-types/bytes) or not.

This function does *not* generate an [event](../../overview/events).

{{% notice warning %}}
This function has a deprecated alias `isbytes` which will be removed in the next *minor* release.
{{% /notice %}}

### Function

`is_bytes(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type `bytes`,  else it returns `false`.

### Example

> This code shows some return values for ***is_bytes()***:

```thingsdb,json_response
[
    is_bytes( bytes() ),
    is_bytes( 'abc' ),
];
```

> Return value in JSON format

```json
[
    true,
    false
]
```
