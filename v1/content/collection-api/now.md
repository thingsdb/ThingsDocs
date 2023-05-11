---
title: "now"
weight: 268
---

Return the time in seconds since the epoch as a [floating point](../../data-types/float) number.

If you require the *same* time multiple times within a query,
then call `now()` only once and save it to a [variable](../../overview/variable), for example `now = now();`

This function does *not* generate a [change](../../overview/changes).

### Function

`now()`

### Arguments

None

### Return value

Current timestamp.

### Example

> This code shows the current timestamp:

```thingsdb,should_pass
// current timestamp
now();
```

> Example return value in JSON format

```json
1551093313.6622682
```
