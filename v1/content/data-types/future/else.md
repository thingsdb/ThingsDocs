---
title: "else"
weight: 64
---

Function *else* accepts a [closure](../../closure) as argument which
will be executed *only* when the future is using a module which has failed with some error.
The code inside the closure will only generate a *change* when the closure code is executed.
The return value of the closure will be used as the new future value.

The closure will be called with the same arguments as given to the future, except for the first argument, which is the error from the module.

This function does *not* generate a [change](../../../overview/changes).

### Function

*future*.`else(closure)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure (required) | Closure when will be executed when successful

### Return value

Returns the parent future.

### Example

> This code shows an example using ***then()***:

```thingsdb,json_response,@t
// This module will not work since `dummy` does not exist
new_module('DUMMY', 'dummy');

// Some values for this example
a = 6;
b = 7;

future({
    module: 'DUMMY'
}, a, b).else(|err, a, b| {
    assert( is_err(err) );  // the first argument is of type `error`
    assert (a * b == 42 );  // arguments are also available in the `else` case

    err.msg();              // set the error message as return value
});
```

> Example return value in JSON format

```json
"module `DUMMY` is not running (status: module not installed)"
```
