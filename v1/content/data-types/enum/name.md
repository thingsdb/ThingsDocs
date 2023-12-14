---
title: "name"
weight: 52
---

Returns the name of the enumerator member.

This function does *not* generate a [change](../../../overview/changes).

### Function

*member*.`name()`

### Arguments

None

### Return value

Returns the name of the enumerator member.

### Example

> This code creates a closure with a doc string:

```thingsdb,json_response
set_enum("Color", {
    RED: '#f00'
});

// Return the name of Color{RED}
Color{RED}.name();
```

> Return value in JSON format

```json
"RED"
```
