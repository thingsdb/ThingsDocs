---
title: "starts_with"
weight: 133
---

Determines if a [string](..) starts with characters given by another string.

This function does *not* generate a [change](../../../overview/changes).

### Function

*str*.`starts_with(search_string)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
search_string | str (required) | The characters to be searched for at the start of this string.

### Return value

Returns `true` if the given characters are found at the start of the string and otherwise `false`.

### Example

> This code shows an example using ***starts_with()***:

```thingsdb,json_response
'the answer to life the universe and everything'.starts_with('the answer');
```

> Return value in JSON format

```json
true
```
