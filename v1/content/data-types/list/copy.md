---
title: "copy"
weight: 62
---

Copy a *list*.

If a *deep* value higher than `0` *(default)* is used, then this function will create copies of the *things* within the list.

This function does *not* generate a [change](../../../overview/changes).

### Function

*list*.`copy([deep]])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
deep | int (optional) | How *deep* to copy things withing the list. Default is `0` *(only a copy of the list, not the things within the list)*.

### Return value

A new list.

### Example

> This code shows an example using ***copy()***:

```thingsdb,json_response
x = {x: 123};
a = [x];
b = a.copy();

// both `a` and `b` have thing `x`
assert ( a.has(x) );
assert ( b.has(x) );

// `b` is a copy, so when changing `a`, list `b` remains unaffected.
a.clear();

b;
```

> Return value in JSON format

```json
[
    {
        "x": 123
    }
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

s = [p];

// deep 1 will not only copy the list, but also the things within the list
o = s.copy(1);

// the new list `o` does not have `p` since a copy of `p` is created
assert ( o.has(p) == false );

// copy does not preserve the Type information, the Type for each member is now a normal thing:
o.map(|t| type(t));
```

> Return value in JSON format

```json
[
    "thing"
]
```

