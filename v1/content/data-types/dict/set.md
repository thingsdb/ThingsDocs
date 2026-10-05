---
title: "set"
weight: 71
---

Sets an item in a [dict](..). If the key already exists, the old value will be overwritten.

This function generates a [change](../../../overview/changes).

### Function

*dict*.`set(name, value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
name | uuid/int/str (required) | The key of the item to set.
value | any (required)  | The value to assign to the key.

### Return value

The value that was set.

### Example

> This code shows how to use ***set()***:

```thingsdb,json_response
d = dict();
d.set(42, 'The answer to everything!');
```

> Return value in JSON format

```json
"The answer to everything!"
```
