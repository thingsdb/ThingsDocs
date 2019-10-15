---
title: "type"
date: 2019-10-14T10:06:09+02:00
weight: 58
---

Returns the type name of a value.

This function does *not* generate an [event](../../events).

### Function
`type(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to return the type name for.

### Return value
Type name of the given value.

> Returns the type name of a given value:

```
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
