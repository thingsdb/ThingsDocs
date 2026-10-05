---
title: "copy"
weight: 61
---

Copy a *dict*.

If a *deep* value higher than `0` *(default)* is used, then this function will create copies of the potential *things* within the dict values.

This function does *not* generate a [change](../../../overview/changes).

### Function

*dict*.`copy([deep]])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
deep | int (optional) | How *deep* to copy things withing the dict. Default is `0` *(only a copy of the dict, not the potential things within the dict values)*.

### Return value

A new dict.

### Example

> This code shows an example using ***copy()***:

```thingsdb,json_response
key = uuid('00000000-0000-0000-0000-000000000000');
x = {x: 123};
a = dict([[key, x]]);
b = a.copy();

// both `a[key]` and `b[key]` are the same thing
assert ( a[key] == b[key] );

// `b` is a copy, so when changing `a`, dict `b` remains unaffected.
a.clear();

b;
```

> Return value in JSON format

```json
[
    [
        "00000000-0000-0000-0000-000000000000",
        {
            "x": 123
        }
    ]
]
```

> Note that a copy with a deep value can create copies of things but the Type information will be lost:

```thingsdb,json_response
set_type('Person', {
    name: 'str'
});

p = Person{
    name: 'Foo'
};

d = dict([[0, p]]);

// deep 1 will not only copy the dict, but also the things within the dict
o = d.copy(1);

// the new dict `o[0]` is not equal to `p` since a copy of `p` is created
assert ( o[0] != p );

// copy does not preserve the Type information, the Type for each member is now a normal thing:
o.map(|_, t| type(t));
```

> Return value in JSON format

```json
[
    "thing"
]
```

