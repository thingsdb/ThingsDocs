---
title: "isbool"
weight: 101
---

This function determines whether the value passed to this function
is a [bool](../../data-types/bool) or not.

This function does *not* generate an [event](../../overview/events).

### Function

`isbool(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` is the passed value is a boolean else it returns `false`.

### Example

> This code shows some return values for ***isbool()***:

```thingsdb,json_response
[
    isbool( true ),
    isbool( 'true' ),
    isbool( nil ),
];
```

> Return value in JSON format

```json
[
    true,
    false,
    false
]
```
