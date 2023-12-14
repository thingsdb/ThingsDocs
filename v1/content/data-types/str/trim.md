---
title: "trim"
weight: 137
---

This function can be used to remove all white-space characters from both the start and end of a string.
Whitespace characters include spaces, tabs, new-line characters etc.

This function does *not* generate a [change](../../../overview/changes).

### Function

*str*.`trim()`

### Arguments

None

### Return value

Returns a new string with whitespace characters removed from the start and end of the string.

### See also

- [trim_left](../trim_left)
- [trim_right](../trim_right)

### Example

> Example using ***trim()***:

```thingsdb,json_response
'  Hello World!!  '.trim();
```

> Return value in JSON format

```json
"Hello World!!"
```
