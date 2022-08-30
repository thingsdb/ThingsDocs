---
title: "restrict"
weight: 165
---

Set or remove a value restriction on a thing. Function [restriction()](../restriction) can be used to view the current restriction.

This function generates a [change](../../../overview/changes).

### Function

*thing*.`restrict(type)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str/nil (required) | Restriction to set on the thing or `nil` to remove a restriction.

### Return value

Returns the thing

### Example

> Use `restrict()` to force int values on a thing;

```thingsdb,json_response
example = {}.restrict('int');
example.x = 10;
assert ( is_err ( try ( example.name = 'Iris' )));  // values must be float
example;
```

> Return value in JSON format

```json
{
    "x": 10
}
```
