---
title: "value"
weight: 38
---

Returns the value of the enumerator member.

This function does *not* generate an [event](../../../overview/events).

### Function

*member*.`value()`

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

val = Color{RED}.value();

assert( isstr( val ) );  // the value is of type `str`

val.upper();  // Return the value upper case
```

> Return value in JSON format

```json
"#F00"
```
