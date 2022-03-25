---
title: "len"
weight: 93
---

Returns the length of [mpdata](..) in bytes.

This function does *not* generate a [change](../../../overview/changes).

### Function

*mpdata*.`len()`

### Arguments

None

### Return value

Returns length in bytes.

### Example

> This code uses `len()`:

```thingsdb,should_pass,@t
user_info('admin').len();
```

> Example return value in JSON format (size may be different)

```json
358
```
