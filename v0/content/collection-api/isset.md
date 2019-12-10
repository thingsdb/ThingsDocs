---
title: "isset"
weight: 111
---

This function determines whether the value passed to this function
is a [set](../../data-types/set) or not.

This function does *not* generate an [event](../../overview/events).

### Function

`isset(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` is the passed value is a `set`, else it returns `false`.

### Example

> This code shows some return values for ***isset()***:

```thingsdb,json_response
[
    isset( [] ),
    isset( set() ),
];
```

> Return value in JSON format

```json
[
    false,
    true
]
```
