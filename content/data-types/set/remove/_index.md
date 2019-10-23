---
title: "remove"
date: 2019-10-23T13:52:43+02:00
weight: 6
---

This function can be used to remove `things` from a `set`.

If a closure is used, then all things that satisfy the test are removed from the set
and returned as list. The order of the removed things is not guaranteed since the set itself
is unordered.

It is also possible to specify `things` as arguments. In this case a list is returned with
all the things which are removed from the set, in the order that the arguments are used.
Things which are not found in the set are ignored.

This function generates an [event](../../../events).

### Function
*set*.`remove(callback)`

Or

*set*.`remove(thing1, thing2, ..., thingX)`

### Arguments
Explanation of the *callback* argument:

Iterable | Arguments | Description
-------- | -------- | -----------
set | thing, thing ID | Iterate over things in the set. Both `thing` and `thing ID` are optional.

### Return value
A list with the removed `things` from the set or an empty list if nothing is removed.

> This code shows an example using ***remove()*** on a set:

```thingsdb,should_pass
t1 = {x:1}; t2 = {x:2}; t3 = {x:3}; t4 = {x:4};
s = set(t1, t2, t3, t4);
[
    s.remove(|t| t.x < 3),
    s.remove(t1, t2, t3, t4),
]
```

> Example return value in JSON format

```json
[
    [
        {
            "x": 1
        },
        {
            "x": 2
        }
    ],
    [
        {
            "x": 3
        },
        {
            "x": 4
        }
    ]
]
```
