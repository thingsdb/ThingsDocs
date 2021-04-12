---
title: "len"
weight: 83
---

Returns the length of [mpdata](..) in bytes.

This function does *not* generate an [event](../../../overview/events).

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
