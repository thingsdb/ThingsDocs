---
title: "has_procedure"
weight: 382
---

Determines if a procedure exists in the current scope.

This function does *not* generate a [change](../../overview/changes).

### Function

`has_procedure(procedure)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
procedure | str (required) | Procedure name to check.

### Return value

Returns `true` if a procedure with a given name exists in the current scope and otherwise `false`.

### Example

> This code shows an example use case of ***has_procedure()***:

```thingsdb,json_response,@t
has_procedure('I_most_likely_do_not_exist');
```

> Return value in JSON format

```json
false
```
