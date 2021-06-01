---
title: "trim_right"
weight: 114
---

This function can be used to remove all white-space characters from the end of a string.
Whitespace characters include spaces, tabs, new-line characters etc.

This function does *not* generate an [event](../../../overview/events).

### Function

*str*.`trim_right()`

### Arguments

None

### Return value

Returns a new string with whitespace characters removed from the end of the string.

### See also

- [trim](../trim)
- [trim_left](../trim_left)

### Example

> Example using ***trim_right()***:

```thingsdb,json_response
'  Hello World!!  '.trim_right();
```

> Return value in JSON format

```json
"  Hello World!!"
```
