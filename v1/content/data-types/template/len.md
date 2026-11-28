---
title: "len"
weight: 190
---

Returns the length of the raw template.

This function does *not* generate a [change](../../../overview/changes).

### Function

*template*.`len()`

### Arguments

None

### Return value

Returns the length of the raw template.

### Example

> This code uses `len()` to return the length of the template:

```thingsdb,json_response
tpl = template("Hello {name}!");
tpl.len();
```

> Return value in JSON format

```json
13
```
