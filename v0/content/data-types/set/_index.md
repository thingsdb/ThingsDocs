---
title: "set"
weight: 56
---

A set is a collection which is unordered and can only contain things.
Each [thing](../thing) will only exists once in a collection.

### Functions

Function | Description
------ | -----------
[add](./add) | Add things to a set.
[each](./each) | Iterate over all items in a set.
[filter](./filter) | Return a new `set` with things that pass a given test.
[find](./find) | Return the first `thing` which passes a given test.
[has](./has) | Test if a set contains a given thing.
[len](./len) | Return the length of a set.
[map](./map) | Return a [list](../list) with the results of calling a provided closure on every thing.
[remove](./remove) | Remove things from a set.

### Operators

Operation | Description
--------- | -----------
`|` *(union)* | Set with things from both `a` and `b`.
`&` *(intersection)* | Set with things common to `a` and `b`.
`-` *(difference)* | Set with things in `a` but not in `b`.
`^` *(symmetric difference)* | Set with things in either `a` or `b` but not both.

> Example set operators

```thingsdb,should_pass
anna = {};
cato = {};
iris = {};

a = set(cato, iris);
b = set(cato, anna);

assert (a | b == set(anna, cato, iris));    // Union
assert (a & b == set(cato));                // Intersection
assert (a - b == set(iris));                // Difference
assert (a ^ b == set(anna, iris));          // Symmetric difference
```

{{% notice warning %}}
Be careful using assignment operators on *stored* sets. Although set operations are processed very efficient, a change to a *stored* set requires an event. This event is still an *assignment* and
will therefore contain the **complete resulting set**. \
In practice this means that it is perfect to write something like `set_a |= set_b`, but avoid using a stored set like `.set_a |= set_b`.
{{% /notice %}}


### Related functions

Function | Description
------ | -----------
[set](../../collection-api/set) | Create a new empty set or convert a [list](../list) to a new set.

