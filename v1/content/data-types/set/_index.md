---
title: "set"
weight: 118
---

A set is a collection which is unordered and can only contain things.
Each [thing](../thing) will only exists once in a collection.

### Functions

Function | Description
------ | -----------
[add](./add) | Add things to a set.
[clear](./clear) | Remove all things from a set.
[copy](./copy) | Copy a set *(same as [dup](./dup) unless a non-zero deep argument is used)*.
[dup](./dup) | Duplicate a set.
[each](./each) | Iterate over all items in a set.
[every](./every) | Check if all things pass a given test.
[filter](./filter) | Return a new `set` with things that pass a given test.
[find](./find) | Return the first `thing` which passes a given test.
[has](./has) | Test if a set contains a given thing.
[len](./len) | Return the length of a set.
[map](./map) | Return a [list](../list) with the results of calling a provided closure on every thing.
[map_id](./map_id) | Return a `list` with the Ids for all the *things* in the original *set*.
[map_wrap](./map_wrap) | Return a `list` with the Ids for all the *things* in the original *set*.
[one](./one) | Return one _thing_ from the set.
[reduce](./reduce) | Execute a reducer function on each thing, resulting in a single output value.
[remove](./remove) | Remove things from a set. Accepts one or more things to remove or a closure to be used as a test. The removed things are returned in a list.
[restriction](./restriction) | Return the restriction of the set or `nil` when the set is not restricted.
[some](./some) | Check if at least one thing passes a given test.

### Operators

Operation | Description
--------- | -----------
`\|` *(union)* | Set with things from both `a` and `b`.
`&` *(intersection)* | Set with things common to `a` and `b`.
`-` *(difference)* | Set with things in `a` but not in `b`.
`^` *(symmetric difference)* | Set with things in either `a` or `b` but not both.
`<=` *(is subset)* | Determines if `a` is a subset of `b`.
`<` *(is proper subset)* | Determines if `a` is a proper subset of `b` _(subset, but not equal)_.
`>=` *(is superset)* | Determines if `a` is a superset of `b`.
`>` *(is proper superset)* | Determines if `a` is a proper superset of `b` _(superset, but not equal)_.

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

assert (a < set(anna, cato, iris));         // "a" is a proper subset
assert ((a < set(cato, iris)) == false);    // "a" is not a proper subset
assert (a <= set(cato, iris));              // "a" is a subset
assert ((a <= b) == false);                 // "a" is not a subset of "b"
assert (a > set(iris));                     // "a" is a superset of set(iris)

```

{{% notice warning %}}
Be careful using assignment operators on *stored* sets. Although set operations are processed very efficient, a change to a *stored* set requires a *change*. This *change** is still an *assignment* and
will therefore contain the **complete resulting set**. \
In practice this means that it is perfect to write something like `set_a |= set_b`, but avoid using a stored set like `.set_a |= set_b`.
{{% /notice %}}

### Related functions

Function | Description
------ | -----------
[set](../../collection-api/set) | Create a new empty set or convert a [list](../list) to a new set.
