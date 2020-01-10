---
title: "doc"
weight: 27
---

Returns a doc string from a [closure](..).

An empty string (`""`) is returned if the closure has no doc string.

This function does *not* generate an [event](../../../overview/events).

### Function

*closure*.`doc()`

### Arguments

None

### Return value

Returns the doc string.

### Example

> This code creates a closure with a doc string:

```thingsdb,json_response
add_one = |x| {
    "Adds one to a given value.";
    x+1;
};

// Return the doc string
add_one.doc();
```

> Return value in JSON format

```json
"Adds one to a given value."
```
