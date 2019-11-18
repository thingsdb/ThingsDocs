---
title: "wse"
weight: 157
---

Stored closures which can potentially make changes to ThingsDB are called
*closures with side effects* and must be wrapped with the `wse(..)` function.

This allows ThingsDB before running the query to make an event.
You should not wrap `wse` around all closures since this would unnecessary
create events when they may not be required.

This function generates an [event](../../events).

### Function

`wse(statement)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
statement | any | Statement or block to wrap.

### Return value

Return value of the given statement.

> This code shows an example usage for ***wse()***:

```thingsdb,json_response
// Suppose we have a closure with side-effects
.take_license = || .licenses -= 1;

// And we have some initial licenses
.licenses = 99;

wse({
    // without wse() this would raise an error
    .take_license.call();
});

// Return the number of licenses left
.licenses;
```

> Return value in JSON format

```json
98
```
