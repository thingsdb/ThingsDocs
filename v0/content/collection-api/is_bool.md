---
title: "is_bool"
weight: 145
---

This function determines whether the provided value is a [bool](../../data-types/bool) or not.

This function does *not* generate an [event](../../overview/events).

{{% notice warning %}}
This function has a deprecated alias `isbool` which will be removed in the next *minor* release.
{{% /notice %}}

### Function

`is_bool(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is a boolean, else it returns `false`.

### Example

> This code shows some return values for ***is_bool()***:

```thingsdb,json_response
[
    is_bool( true ),
    is_bool( 'true' ),
    is_bool( nil ),
];
```

> Return value in JSON format

```json
[
    true,
    false,
    false
]
```
