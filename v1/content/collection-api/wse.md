---
title: "wse"
weight: 283
---

This function enforces ThingsDB to create a [change](../../overview/changes).

When using a stored closure which requires a change it might not be possible for ThingsDB
to detect the change requirement before evaluation the query. In this case it is required to use `wse()` to enforce a change.

Function `wse()` might both wrap a statement and be called without arguments.

This function generates a [change](../../overview/changes).

### Function

`wse([statement])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
statement | any (optional) | Statement or block to wrap.

### Return value

Return value of the given statement.

### Example

> This code shows an example usage for ***wse()***:

```thingsdb,should_pass
// Suppose we have a closure with side-effects
.take_license = || .licenses -= 1;

// And we have some initial licenses
.licenses = 99;
```

> Here we need **wse()** to enforce a change:

```thingsdb,syntax_only
wse();

// without wse() no change would be created and thus this would raise an error
.take_license();

// Return the number of licenses left
.licenses;
```

> Return value in JSON format

```json
98
```
