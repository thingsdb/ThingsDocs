---
title: "then"
weight: 86
---

Function *then* accepts a [closure](../../closure) as an argument which
will be executed *only* when the future succeeds. The code inside the closure
will only generate a [change](../../../overview/changes) when the closure code is actually executed. The return value of the
closure will be used as the new future value.

The closure receives the future's result as its first argument, followed by any additional arguments passed to the future. When calling `future(nil, ...)`, the request is purely asynchronous and produces no module result, so the first argument will be `nil` (commonly ignored using `_`). When chaining `.then(..)` onto a module call (such as `requests.get(..)`), the first argument contains the response returned by the module.

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

> Using ***then()*** with `future(nil, ...)` for an asynchronous calculation (where `_` ignores the `nil` result):

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


> Using ***then()*** with a module call (assuming the `requests` module is installed):

```thingsdb,syntax_only
// Install the requests module in @thingsdb scope if not already present:
// new_module('requests', 'https://github.com/thingsdb/module-go-requests');

requests.get('https://example.com').then(|res| {
    // `res` contains the response from the module
    res.status_code;
});
```