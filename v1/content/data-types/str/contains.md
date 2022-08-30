---
title: "contains"
weight: 124
---

Determines if a given string is a substring of a [string](..).

This function does *not* generate a [change](../../../overview/changes).

### Function

*str*.`contains(search_string)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
search_string | str (required) | The characters to be searched for in the string.

### Return value

Returns `true` if the given characters are found as a substring and otherwise `false`.

### Example

> This code shows an example using ***contains()***:

```thingsdb,json_response
'the answer to life the universe and everything'.contains('life');
```

> Return value in JSON format

```json
true
```
