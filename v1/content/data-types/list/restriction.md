---
title: "restriction"
weight: 87
---

Returns the lst restriction as type [str](../../str) or [nil](../../nil) when the list is *not* value restricted.

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`restriction()`

### Arguments

None

### Return value

Returns restriction of the list or `nil` if *not* value restricted.

### Example

> Using `restriction()` on a non-restricted list:

```thingsdb,json_response
[1, 2, 3, 4].restriction();
```

> Return value in JSON format

```json
null
```

> Using `restriction()` on a restricted list:

```thingsdb,json_response
// Create an example type
set_type('X', {arr: '[int]'});

X{}.arr.restriction();
```

> Return value in JSON format

```json
"int"
```