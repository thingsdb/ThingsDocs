---
title: "len"
weight: 77
---

Returns the length of a [string](..).

{{% notice warning %}}
Be aware that the length represents the number of *bytes* and not the number of *characters*. see example below.
{{% /notice %}}

This function does *not* generate an [event](../../../overview/events).

### Function

*str*.`len()`

### Arguments

None

### Return value

Returns length of the string.

### Example

> This code uses `len()` to return the length of a string:

```thingsdb,json_response
[
    {'Hello'.len();  /* 5 bytes */ },
    {'π'.len();      /* 2 bytes, not 1 */ },
]
```

> Return value in JSON format

```json
[
    5,
    2
]
```
