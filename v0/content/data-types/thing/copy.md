---
title: "copy"
weight: 115
---

Copy a *thing*.

{{% notice warning %}}
The function does *not* preserve the Type of a thing. Use [dup(..)](../dup) if you want a copy of the same type.
{{% /notice %}}

This function does *not* generate an [event](../../../overview/events).

### Function

*thing*.`copy([deep]])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
deep | int (optional) | How *deep* to copy the thing. Default is `1`.

### Return value

A new thing.

### Example

> This code shows an example using ***copy()***:

```thingsdb,json_response
a = {x: 123};
b = a.copy();

// `b` is a copy, so `a.x` will not change
b.x = 456;

[a.x, b.x];
```

> Return value in JSON format

```json
[
    123,
    456
]
```

> Note that a copy is a new thing and Type information will be lost:

```thingsdb,json_response
set_type('Person', {
    name: 'str'
});

p = Person{
    name: 'Foo'
};

o = p.copy();

type(o);  // just a normal `thing`
```

> Return value in JSON format

```json
"thing"
```

