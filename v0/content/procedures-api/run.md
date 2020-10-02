---
title: "run"
weight: 239
---

Run a procedure.

This function does *not* generate an [event](../../overview/events).

### Function

`run(procedure, ...args)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
procedure | str (required) | Name of the procedure to run.
...args | any | The arguments for the procedure. If more arguments are given than the procedure expects, the redundant arguments will be ignored. If too few arguments are given, then the remaining arguments will be set to nil.

### Return value

Returns the procedure response.

### Example

> Example code using *run*:

```thingsdb,json_response
// create a greet procedure
new_procedure('greet', |name| is_str(name)
    ? "Hello " + name
    : "Hello unnamed user!"
);

// run `greet` with a given name
greet_iris = run('greet', "Iris");

// run `greet` with nil
greet_nil = run('greet', nil);

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
