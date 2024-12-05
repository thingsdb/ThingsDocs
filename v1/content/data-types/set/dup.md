---
title: "dup"
weight: 122
---

Duplicate a *set*.

If a *deep* value higher than `0` *(default)* is used, then this function will also create duplicates of the *things* within the set.

This function does *not* generate a [change](../../../overview/changes).

### Function

*set*.`dup([deep]])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
deep | int (optional) | How *deep* to duplicate things withing the set. Default is `0` *(only a duplicate of the set, not the things within the set)*.

### Return value

A new set.

### Example

> This code shows an example using ***dup()***:

```thingsdb,json_response
x = {x: 123};
a = set(x);
b = a.dup();

// both `a` and `b` have thing `x`
assert ( a.has(x) );
assert ( b.has(x) );

// `b` is a duplicate, so when changing `a`, set `b` remains unaffected.
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

> Note that a duplicate with a deep value can create duplicates of things with the Type information preserved:

```thingsdb,json_response
set_type('Person', {
    name: 'str'
});

p = Person{
    name: 'Foo'
};

s = set(p);

// deep 1 will not only duplicate the set, but also the things within the set
o = s.dup(1);

// the new set `o` does not have `p` since a duplicate of `p` is created
assert ( o.has(p) == false );

// duplicate does preserve the Type information, the Type for each member is unaffected
o.map(|t| type(t));
```

> Return value in JSON format

```json
[
    "Person"
]
```

