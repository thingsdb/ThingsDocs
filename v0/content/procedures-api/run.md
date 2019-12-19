---
title: "run"
weight: 180
---

Run a procedure.

This function does *not* generate an [event](../../overview/events).

### Function

`run(procedure, ...args)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
procedure | str (required) | Name of the procedure to run.
...args | any | The exact number of arguments for the procedure must be given.

### Return value

Returns the procedure response.

### Example

> Example code using *run*:

```thingsdb,json_response
// create a greet procedure
new_procedure('greet', |name| isstr(name)
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

