---
title: "restriction"
weight: 168
---

Returns the value restriction of a thing as type [str](../../str) or [nil](../../nil) when the thing is *not* value restricted. A thing can be restricted when the thing is a property of a *typed* thing or by using the [restrict(..)](../restrict) function (see the [example](#example)).

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

> Using `restriction()` on a another restricted thing:

```thingsdb,json_response
// Create an example type
set_type('X', {onlyint: 'thing<int>'});

X{}.onlyint.restriction();
```

> Return value in JSON format

```json
"int"
```
