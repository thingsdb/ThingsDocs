---
title: "isset"
weight: 143
---

This function determines whether the provided value is a [set](../../data-types/set) or not.

This function does *not* generate an [event](../../overview/events).

### Function

`isset(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is a `set`, else it returns `false`.

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
