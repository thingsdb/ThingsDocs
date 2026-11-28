---
title: "has_var"
weight: 261
---

Determines if a variable exists in the current scope.

This function does *not* generate a [change](../../overview/changes).

### Function

`has_var(var)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
var | str (required) | Variable name to check.

### Return value

Returns `true` if a variable with the given name exists in the current scope (even if its value is `nil`) and otherwise `false`.

### Example

> This code shows an example use case of ***has_var()***:

```thingsdb,json_response
x = nil;
[
    has_var('x'),
    has_var('y'),
];
```

> Return value in JSON format

```json
[
    true,
    false
]
```