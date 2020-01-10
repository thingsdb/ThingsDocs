---
title: "call"
weight: 26
---

Call a closure.

This function does *not* generate an [event](../../../overview/events).

### Function

*closure*.`call()`

### Arguments

The exact number of arguments for the closure must be given.

{{% notice tip %}}
It is not possible to assign default values to arguments but something similar
can be accomplished by checking the argument within the closure. See the example below.
{{% /notice %}}

### Return value

Returns the closure response.

### Example

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

