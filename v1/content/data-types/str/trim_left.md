---
title: "trim_left"
weight: 127
---

This function can be used to remove all white-space characters from the start of a string.
Whitespace characters include spaces, tabs, new-line characters etc.

This function does *not* generate a [change](../../../overview/changes).

### Function

*str*.`trim_left()`

### Arguments

None

### Return value

Returns a new string with whitespace characters removed from the start of the string.

### See also

- [trim](../trim)
- [trim_right](../trim_right)

### Example

> Example using ***trim_left()***:

```thingsdb,json_response
'  Hello World!!  '.trim_left();
```

> Return value in JSON format

```json
"Hello World!!  "
```
