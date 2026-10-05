---
title: "dup"
weight: 63
---

Duplicate a *dict*.

If a *deep* value higher than `0` *(default)* is used, then this function will also create duplicates of the *things* within the dict.

This function does *not* generate a [change](../../../overview/changes).

### Function

*dict*.`dup([deep]])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
deep | int (optional) | How *deep* to duplicate things withing the dict. Default is `0` *(only a duplicate of the dict, not the things within the dict)*.

### Return value

A new dict.

### Example

> This code shows an example using ***dup()***:

```thingsdb,json_response
key = uuid('00000000-0000-0000-0000-000000000000');
x = {x: 123};
a = dict([[key, x]]);
b = a.dup();

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

> Note that a duplicate with a deep value can create duplicates of things with the Type information preserved:

```thingsdb,json_response
dict_type('Person', {
    name: 'str'
});

p = Person{
    name: 'Foo'
};

d = dict([[0, p]]);

// deep 1 will not only duplicate the dict, but also the things within the dict
o = d.dup(1);

// the new dict `o[0]` is not equal to `p` since a duplicate of `p` is created
assert ( o[0] != p );

// duplicate does preserve the Type information, the Type for each member is unaffected
o.map(|_, t| type(t));
```

> Return value in JSON format

```json
[
    "Person"
]
```

