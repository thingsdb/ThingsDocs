---
title: "closure"
weight: 300
---

Closures can be used to consume items from a `thing`, `list`, `tuple` or `set`.
They are also used by [procedures](../../procedures-api) where they get the role of a function.

The following syntax is used to define a closure

```thingsdb,no_test
|argument1,... argumentX| ...
```

Closure may like any value, be stored in a collection or assigned to a variable.

> For example:

```thingsdb,json_response
// create a simple closure which just adds one to a given value
add_one = |x| x+1;

// use the closure in a `map` function
map_result = [1, 2, 3].map(add_one);

// use the closure as a function call
call_result = add_one.call(41);

// return the result values
[map_result, call_result];
```

> Return value in JSON format
```json
[
    [
        2,
        3,
        4
    ],
    42
]
```

### Methods

Method | Description
------ | -----------
[call](./call) | Call the closure with optional arguments.


{{% notice note %}}
It is not possible to use closures with recursion, for example:
`a = ||.map(a); .map(a);` \
...will raise `OPERATION_ERROR` *(closures cannot be used recursively)*
{{% /notice %}}
