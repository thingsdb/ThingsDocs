---
title: "restriction"
weight: 154
---

Returns the value restriction of a thing as type [str](../../str) or [nil](../../nil) when the thing is *not* value restricted.

This function does *not* generate a [change](../../../overview/changes).

### Function

*thing*.`restriction()`

### Arguments

None

### Return value

Returns restriction of the thing or `nil` if *not* value restricted.

### Example

> Using `restriction()` on a non-restricted thing:

```thingsdb,json_response
{}.restriction();
```

> Return value in JSON format

```json
null
```

> Using `restriction()` on a restricted thing:

```thingsdb,json_response
{}.restrict('str').restriction();
```

> Return value in JSON format

```json
"str"
```