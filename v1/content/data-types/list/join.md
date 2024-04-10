---
title: "join"
weight: 84
---

This function returns a new string by concatenating all items in a [list](..) or [tuple](../../tuple).
All items in the list or tuple must be of type [str](../../str), otherwise a [type_err()](../../../errors/type_err) is raised.

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`join([separator])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
separator | str (optional) | Optional separator. The default separator is an empty string (`""`) which results in a string with all items joined without any characters in between.

### Return value

Returns a string with all items joined. An empty string is returned if the list or tuple is empty.

### Example

> This code shows an example using ***join()***:

```thingsdb,json_response
// Returns a new string
['Hello', 'ThingsDB'].join(" ");
```

> Return value in JSON format

```json
"Hello ThingsDB"
```
