---
title: "call"
weight: 310
---

Call a closure with optional arguments.

This function does *not* generate an [event](../../../events).

### Function
*closure*.`call()`

### Arguments
The exact number of arguments which the closure accepts must be given.
It is not possible to assign default values to arguments but something similar
can be accomplished by checking the argument within the closure. See the example.

### Return value
Returns the closure response.

> Example code using *call*:

```thingsdb,json_response
// create a greet closure
greet = |name| isstr(name)
    ? "Hello " + name
    : "Hello unnamed user!";

// call with a given name
greet_iris = greet.call("Iris");

// call with nil
greet_nil = greet.call(nil);

// return the greet response values
[greet_iris, greet_nil];
```

> Return value in JSON format
```json
[
    "Hello Iris",
    "Hello unnamed user!"
]
```

