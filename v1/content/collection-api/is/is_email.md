---
title: "is_email"
weight: 239
---

This function determines whether the provided value is of
type [str](../../../data-types/str) and contains an email address.

This function does *not* generate a [change](../../../overview/changes).

### Function

`is_email(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type `str` and contains an email address, else `false`.

### Example

> This code shows some return values for ***is_email()***:

```thingsdb,json_response
[
    is_email( 'info@thingsdb.io' ),
    is_email( 'test' ),
];
```

> Return value in JSON format

```json
[
    true,
    false
]
```
