---
title: "then"
weight: 54
---

Function *then* accepts a [closure](../../closure) as argument which
will be executed *only* when the future is successful. The code inside the closure
will only generate a *change* then the closure code is executed. The return value of the
closure will be used as the new future value.

The closure will be called with the same arguments as given to the future, except for the first argument, which can be the result of a module.

This function does *not* generate a [change](../../../overview/changes).

### Function

*future*.`then(closure)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure (required) | Closure when will be executed when successful

### Return value

Returns the parent future.

### Example

> This code shows an example using ***then()***:

```thingsdb,json_response
a = 6;
b = 7;
future(nil, a, b).then(|_, a, b| {
    a * b;
});
```

> Example return value in JSON format

```json
42
```
