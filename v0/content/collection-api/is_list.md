---
title: "is_list"
weight: 166
---

This function determines whether the provided value is a [list](../../data-types/list) or not.

This function does *not* generate an [event](../../overview/events).

{{% notice warning %}}
This function has a deprecated alias `islist` which will be removed in the next *minor* release.
{{% /notice %}}

### Function

`is_list(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is a `list`, else it returns `false`.

### Example

> This code shows some return values for ***is_list()***:

```thingsdb,json_response
[
    is_list( [] ),
    is_list( tmp = [['nested']] ),
    is_list( tmp[0] ),
];
```

> Return value in JSON format

```json
[
    true,
    true,
    false
]
```
