---
title: "return"
weight: 147
---

The `return` function moves the argument to the output of the current query/closure call.

If no `return` is specified, then the last value will be the value which is returned.
A second argument can be given to the return function which can be used to specify how `deep`
the result should be returned. The default `deep` value is set to 1, but any value between 0 and 127 is possible.

A query can run different procedures and/or closures which might have changed the `deep` value. In case you
need to know the current `deep` value, the function [deep()](../../collection-api/deep) can be used.

{{% notice warning %}}
Be careful with using a high deep value, especially when circular references are made since this can result
in returning a large amount of data.
{{% /notice %}}

When no arguments are used the return value will be `nil`.

This function does *not* generate an [event](../../overview/events).

### Function

`return([value[, deep]])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (optional) | The value which will be moved to the output of the query or closure.
deep | int (optional) | Specify the `deep` value for the query (the current `deep` value will be overwritten).

### Return value

The `return` function has no real return value but will move directly
to the output of the current query or closure.

### Example

> This code shows how ***return()*** can be used:

```thingsdb,should_pass
// return .colors, two levels deep if .colors exists
try(return(.colors, 2));

// if .colors could not be returned, create the property
.colors = {
    aegean: {
        R: 0x5e,
        G: 0x8e,
        B: 0xc9,
    },
};

return(.colors, 2);
```

> Example return value in JSON format (the #ids might be different)

```json
{
    "#": 23,
    "aegean": {
        "#": 24,
        "B": 201,
        "G": 142,
        "R": 94
    }
}
```
