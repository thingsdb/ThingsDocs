---
title: "wse"
weight: 132
---

Stored closures which can potentially make changes to ThingsDB are called
*closures with side effects* and must be wrapped with the `wse(..)` function.
This allows ThingsDB before running the query to make an event.

{{% notice info %}}
You should use `wse` only when required since otherwise this would unnecessary
create events.
{{% /notice %}}

This function generates an [event](../../overview/events).

### Function

`wse(statement)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
statement | any | Statement or block to wrap.

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
    .take_license.call();
});

// Return the number of licenses left
.licenses;
```

> Return value in JSON format

```json
98
```
