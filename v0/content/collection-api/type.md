---
title: "type"
weight: 175
---

Returns the type name of a value.

This function does *not* generate an [event](../../overview/events).

### Function

`type(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to return the type name for.

### Return value

Type name of the given value.

### Example

> Returns the type name of a given value:

```thingsdb,json_response
[
    type( nil ),
    type( 42 ),
    type( 3.14 ),
];
```

> Example return value in JSON format

```json
[
    "nil",
    "int",
    "float"
]
```
