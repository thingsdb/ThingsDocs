---
title: "restriction"
weight: 70
---

Returns the dictionary key and value restrictions as a [list](../../list) of two [strings](../../str). The first element represents the key restriction, and the second represents the value restriction. A dict can *only* be restricted when defined as a property of a *typed* thing (see the [example](#example)).

This function does *not* generate a [change](../../../overview/changes).

### Function

*dict*.`restriction()`

### Arguments

None

### Return value

Returns a list containing two strings representing the key and value type restrictions _(e.g., `["uuid", "T"]` for keys of type [uuid](../../uuid) and values of type `T`)_.
If no restriction is set, `["any", "any"]` is returned.

### Example

> Using `restriction()` on a non-restricted dict:

```thingsdb,json_response
dict().restriction();
```

> Return value in JSON format

```json
["any", "any"]
```

> Using `restriction()` on a restricted dict:

```thingsdb,json_response
// Create an example type
set_type('Example', {
    lookup: 'dict<uuid:str>',
});

Example{}.lookup.restriction();
```

> Return value in JSON format

```json
["uuid", "str"]
```