---
title: "restriction"
weight: 128
---

Returns the set restriction as type [str](../../str) or [nil](../../nil) when the set is *not* value restricted. A set can *only* be restricted if the set is a property of a *typed* thing (see the [example](#example)).

This function does *not* generate a [change](../../../overview/changes).

### Function

*set*.`restriction()`

### Arguments

None

### Return value

Returns restriction of the set or `nil` if *not* value restricted.

### Example

> Using `restriction()` on a non-restricted set:

```thingsdb,json_response
set().restriction();
```

> Return value in JSON format

```json
null
```

> Using `restriction()` on a restricted set:

```thingsdb,json_response
// Create an example type
new_type('S');
set_type('Y', {set: '{S}'});

Y{}.set.restriction();
```

> Return value in JSON format

```json
"S"
```