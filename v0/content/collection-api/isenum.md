---
title: "isenum"
weight: 134
---

This function determines whether the provided value is an [enumeration type](../../data-types/enum) member or not.

This function does *not* generate an [event](../../overview/events).

### Function

`isenum(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type `enum`,  else it returns `false`.

### Example

> This code shows some return values for ***isenum()***:

```thingsdb,json_response
set_enum('Status', {
    OK: 0,
    NOK: -1,
});

[
    isenum( Status{OK} ),
    isenum( 0 ),
];
```

> Return value in JSON format

```json
[
    true,
    false
]
```
