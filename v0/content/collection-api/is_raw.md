---
title: "is_raw"
weight: 152
---

This function determines whether the provided value is of
type `str` *or* `bytes`.

This function does *not* generate an [event](../../overview/events).

{{% notice warning %}}
This function has a deprecated alias `israw` which will be removed in the next *minor* release.
{{% /notice %}}

### Function

`is_raw(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type `str` *or* `bytes`, else `false`.

### Example

> This code shows some return values for ***is_raw()***:

```thingsdb,json_response
[
    is_raw( 'some string' ),
    is_raw( bytes('xxxx') ),
];
```

> Return value in JSON format

```json
[
    true,
    true
]
```
