---
title: "is_set"
weight: 157
---

This function determines whether the provided value is a [set](../../data-types/set) or not.

This function does *not* generate an [event](../../overview/events).

{{% notice warning %}}
This function has a deprecated alias `isset` which will be removed in the next *minor* release.
{{% /notice %}}

### Function

`is_set(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is a `set`, else it returns `false`.

### Example

> This code shows some return values for ***is_set()***:

```thingsdb,json_response
[
    is_set( [] ),
    is_set( set() ),
];
```

> Return value in JSON format

```json
[
    false,
    true
]
```
