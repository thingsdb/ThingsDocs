---
title: "closure"
weight: 37
---

Closures are user defined methods which can be saved. They can be used as a prepared piece of code or to consume items from a `thing`, `list`, `tuple` or `set`.
They can also be used by [procedures](../../procedures-api).

Closure can be stored in a collection or assigned to a variable.

A closure starts with a `|`, then takes optional arguments and a `|` to close, followed by a statement.
The most simple closure is `||nil` which is a closure without arguments and returns the value `nil` when called.

More complex closures are also possible, check the last example below.

### Functions

Function | Description
------ | -----------
[call](./call) | Call the closure with optional arguments.
[doc](./doc) | Return the doc string of the closure.

{{% notice note %}}
Closures may be called recursively up to a **recursion depth of 24**. If this limit is exceeded, an error is raised.
For example: `a = ||a(); a();` \
...will raise [operation_err()](../../errors/operation_err) *(maximum recursion depth exceeded)*
{{% /notice %}}

### Doc string

Doc strings can be set on closures. This is especially useful when closures
are used inside a procedure since this gives the procedure a nice documentation string.

Usually, a doc string is just a normal string on top of a block in the closure.

For example:

```thingsdb,should_pass
|| {
    "this is a doc string.";
};
```

It is common to wrap a block scope within one or more functions.
When this is the case, the doc string will be read from the first argument,
*only* if the first *non-function* argument contains a block scope with a doc string.

For example, this closure contains a block scope wrapped with [return](../../overview/statements/#return) and [wse](../../collection-api/wse):

```thingsdb,should_pass
|| return wse({
    "this is still a doc string, even while wrapped using `return` and `wse`.";
}), 2;
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

    assert(is_str(name) && name.len());
    assert(is_int(age) && age >= 0);

    // this is the last statement so it will be the return value
    {
        name: name,
        age: age,
        time: now()
    };
};
```
