---
title: "ends_with"
weight: 114
---

Determines if a [string](..) ends with characters given by another string.

This function does *not* generate a [change](../../../overview/changes).

### Function

*str*.`ends_with(search_string)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
search_string | str (required) | The characters to be searched for at the end of this string.

### Return value

Returns `true` if the given characters are found at the end of the string and otherwise `false`.

### Example

> This code shows an example using ***ends_with()***:

```thingsdb,json_response
'the answer to life the universe and everything'.ends_with('everything');
```

> Return value in JSON format

```json
true
```
