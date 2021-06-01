---
title: "wse"
weight: 235
---

Stored closures which can potentially make changes to ThingsDB are called
*closures with side effects* and must be wrapped with the `wse(..)` function.
This allows ThingsDB before running the query to make an event.

Function `wse()` might also be called without arguments which can be used to force ThingsDB
to generate an event. This might be useful for when it is really important that a query
returns a result based on a state where all previous events are processed.

{{% notice info %}}
You should use `wse` only when required, otherwise this would lead to unnecessary events.
{{% /notice %}}

This function generates an [event](../../overview/events).

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

```thingsdb,json_response
// Suppose we have a closure with side-effects
.take_license = || .licenses -= 1;

// And we have some initial licenses
.licenses = 99;

wse({
    // without wse() this would raise an error
    .take_license();
});

// Return the number of licenses left
.licenses;
```

> Return value in JSON format

```json
98
```
