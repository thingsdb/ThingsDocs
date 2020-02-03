---
title: "closure"
weight: 25
---

Closures can be used to consume items from a `thing`, `list`, `tuple` or `set`.
They are also used by [procedures](../../procedures-api) where they get the role of a function.

Closure can be stored in a collection or assigned to a variable.

A closure starts with a `|`, then takes optional arguments and a `|` to close, followed by a statement.
The most simple closure is `||nil` which is a closure without arguments and returns the value `nil` when called.

More complex closures are also possible, check the last example below.

### Methods

Method | Description
------ | -----------
[call](./call) | Call the closure with optional arguments.
[doc](./doc) | Returns the doc string of the closure.

{{% notice note %}}
It is not possible to use closures with recursion, for example:
`a = ||.map(a); .map(a);` \
...will raise `OPERATION_ERROR` *(closures cannot be used recursively)*
{{% /notice %}}

### Doc string

Doc strings can be set for closures. This is especially useful for when closures
are used inside a procedure but are not common when closures are used for other purposes.

Usually, a doc string is just a normal string on top of a block in the closure.

For example:

```thingsdb,should_pass
|| {
    "this is a doc string.";
};
```

It is common to wrap a block scope within one or more functions.
When this is the case, the doc string will be read from the the first argument,
*only* if the first *non-function* argument contains a block scope with a doc string.

For example, this closure contains a block scope wrapped with [return](../../collection-api/return) and [wse](../../collection-api/wse):

```thingsdb,should_pass
|| return(wse({
    "this is still a doc string, even while wrapped using `return` and `wse`.";
}), 2);
```

### Examples

> This code uses a simple closure together with *map* and *call*:

```thingsdb,json_response
// create a simple closure which just adds one to a given value
add_one = |x| x+1;

// use the closure in a `map` function
map_result = [1, 2, 3].map(add_one);

// use the closure as a function call
call_result = add_one(41);

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

Like explained, closures can accept multiple arguments and may contain a block scope instead of just a single line statement. Here is an example:


```thingsdb,should_pass
|name, age| {
    "Returns a thing with properties `name`, `age` and `time`.";

    assert(isstr(name) && name.len());
    assert(isint(age) && age >= 0);

    // this is the last statement so it will be the return value
    {
        name: name,
        age: age,
        time: now()
    };
};
```
