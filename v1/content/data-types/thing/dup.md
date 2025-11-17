---
title: "dup"
weight: 172
---

Create a duplicate of a *thing*.

{{% notice warning %}}
The function preserves the Type of a thing. Use [copy(..)](../copy) to copy into a plain thing.
{{% /notice %}}

For the *deep* value, this function does *not* inherit the current *deep* value but *always* uses `1` as default.

This function does *not* generate a [change](../../../overview/changes).

### Function

*thing*.`dup([deep]])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
deep | int (optional) | How *deep* to duplicate the thing. Default is `1`.

### Return value

A new thing.

### Example

> This code shows an example using ***dup()***:

```thingsdb,json_response
a = {x: 123};
b = a.dup();

// `b` is a duplicate, so `a.x` will not change
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

> Note that a duplicate keeps the Type information:

```thingsdb,json_response
set_type('Person', {
    name: 'str'
});

p = Person{
    name: 'Foo'
};

o = p.dup();

type(o);  // type `Person`
```

> Return value in JSON format

```json
"Person"
```

