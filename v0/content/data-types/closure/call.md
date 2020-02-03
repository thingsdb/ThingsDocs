---
title: "call"
weight: 26
---

Call a closure.

When assigned to a variable, it is not required to explicitly write the `call` function.
Simply calling the closure by using `()` will work as well.

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

// call with nil, without explicitly writing `.call()`
greet_nil = greet(nil);

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

