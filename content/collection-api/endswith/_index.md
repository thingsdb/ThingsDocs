---
title: "endswith"
date: 2019-10-14T09:58:15+02:00
weight: 9
---

Determines if a string ends with characters given by another string.

This function does *not* generate an [event](../../events).

### Function
*string*.`endswith(search_string)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
search_string | raw (required) | The characters to be searched for at the end of this string.

### Return value
Returns `true` the given characters are found at the end of the string and otherwise `false`.

> This code shows an example using ***endswith()***:

```thingsdb,json_response
'the answer to life the universe and everything'.endswith('everything');
```

> Return value in JSON format

```json
true
```
