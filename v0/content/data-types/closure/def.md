---
title: "def"
weight: 34
---

Returns the [closure](..) definition using spaces, line-breaks and indentation *(4 spaces)*.

This function does *not* generate an [event](../../../overview/events).

### Function

*closure*.`def()`

### Arguments

None

### Return value

Returns the closure definition.

### Example

> This code creates a closure with a doc string:

```thingsdb,json_response
add_one = |x| {
    x + 1;
};

// Return the definition as a string
add_one.def();
```

> Return value in JSON format

```json
"|x| {\n    x + 1;\n}"
```

> Or, when printed:

```text
|x| {
    x + 1;
}
```