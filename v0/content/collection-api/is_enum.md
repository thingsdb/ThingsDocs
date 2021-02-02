---
title: "is_enum"
weight: 169
---

This function determines whether the provided value is an [enumeration type](../../data-types/enum) member or not.

This function does *not* generate an [event](../../overview/events).

{{% notice warning %}}
This function has a deprecated alias `isenum` which will be removed in the next *minor* release.
{{% /notice %}}

### Function

`is_enum(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type `enum`,  else it returns `false`.

### Example

> This code shows some return values for ***is_enum()***:

```thingsdb,json_response
set_enum('Status', {
    OK: 0,
    NOK: -1,
});

[
    is_enum( Status{OK} ),
    is_enum( 0 ),
];
```

> Return value in JSON format

```json
[
    true,
    false
]
```
