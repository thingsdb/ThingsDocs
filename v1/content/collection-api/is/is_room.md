---
title: "is_room"
weight: 252
---

This function determines whether the provided value is a [room](../../../data-types/room) or not.

This function does *not* generate a [change](../../../overview/changes).

### Function

`is_room(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is a `room`, else it returns `false`.

### Example

> This code shows some return values for ***is_room()***:

```thingsdb,json_response
[
    is_room( thing() ),
    is_room( room() ),
];
```

> Return value in JSON format

```json
[
    false,
    true
]
```
