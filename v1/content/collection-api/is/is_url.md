---
title: "is_url"
weight: 265
---

This function determines whether the provided value is of
type [str](../../../data-types/str) and contains a URL. A valid URL must start with either `http:///` , `https://` or `ftp://`.

This function does *not* generate a [change](../../../overview/changes).

### Function

`is_url(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type `str` and contains a URL, else `false`.

### Example

> This code shows some return values for ***is_url()***:

```thingsdb,json_response
[
    is_url( 'www.google.com' ),
    is_url( 'https://thingsdb.io' ),
    is_url( 'http://127.0.0.1/?a=1' ),
];
```

> Return value in JSON format

```json
[
    false,
    true,
    true
]
```
