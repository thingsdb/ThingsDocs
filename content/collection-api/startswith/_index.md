---
title: "startswith"
date: 2019-10-14T10:05:31+02:00
weight: 53
---

Determines if a string starts with characters given by another string.

This function does *not* generate an [event](../../events).

### Function
*string*.`startswith(search_string)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
search_string | raw (required) | The characters to be searched for at the start of this string.

### Return value
Returns `true` the given characters are found at the start of the string and otherwise `false`.

> This code shows an example using ***startswith()***:

```
'the answer to life the universe and everything'.startswith('the answer');
```

> Return value in JSON format

```json
true
```
