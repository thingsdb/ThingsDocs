---
title: "is_regex"
weight: 193
---

This function determines whether the provided value is of type [regex](../../data-types/regex) or not.

This function does *not* generate a [change](../../overview/changes).

### Function

`is_regex(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type [regex](../../data-types/regex), else it returns `false`.

### Example

> This code shows some return values for ***is_regex()***:

```thingsdb,json_response
[
    is_regex( /.*/ ),
    is_regex( regex(".*") ),
    is_regex( ".*" ),
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
