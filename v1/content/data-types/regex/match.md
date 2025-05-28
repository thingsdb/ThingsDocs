---
title: "match"
weight: 118
---

Returns the result of matching a [string](../../str) with the regular expression.

When the regular expression has the global (`g`) flag set, this function returns a list containing all matches; however, capture groups are ignored.
If no matches are found in this mode, an empty list is returned. Conversely, if the global (`g`) flag is ***not*** set, only the first match is returned, and it will include any capture groups.
In this non-global mode, the function returns `nil` if no match is found.


This function does *not* generate a [change](../../../overview/changes).

### Function

*regex*.`match(string)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
string | str (required) | The string to test.

### Return value

- Without the `g` flag: Returns a list containing the first match _(including capture groups)_ if found; otherwise, `nil`.
- With the `g` flag: Returns a list of all matches if found; otherwise, an empty list.

### Example

> Examples using ***match()*** without the `g` flag:

```thingsdb,json_response
r = /version ((\d+\.?)+)/;
r.match("This is version 3.5.1 of the program.");
```

> Return value in JSON format

```json
[
    "version 3.5.1",
    "3.5.1",
    "1"
]
```

> Examples using ***match()*** with the `g` flag:

```thingsdb,json_response
r = /\d+/g;
r.match("The numbers 123 and 456.");
```

> Return value in JSON format

```json
[
    "123",
    "456"
]
```
