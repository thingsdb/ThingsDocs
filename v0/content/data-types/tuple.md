---
title: "tuple"
weight: 68
---

All nested *arrays* are immutable and thus tuples.

```thingsdb,should_pass
list = [];
list.push(['this list will be nested and therefore convert to a tuple']);

// Check that the first item in `list` is indeed a `tuple`
assert(istuple(list[0]));

// Check that the `tuple` is indeed immutable
assert(iserr(try(list[0].push('cannot be added to a tuple'))));
```

A tuple only becomes a `tuple` when it is nested inside a list, which means the 'list' will be immutable.
ThingsDB does this because it wants to update all changes to subscribers and finds the subscribers by the parent object where
the change is  made. Since the parent of a nested 'list' is another list, the `thing` holding the list would not be found.

Another property of `lists` and `tuples` in ThingsDB is that they both are always *copies*, and not by *reference* as in most languages. This is
because ThingsDB needs to know which subscribers to update when changes are made.

### Methods

Method | Description
------ | -----------
[filter](../list/filter) | Returns a new `list` with elements that pass a given test.
[find](../list/find) | Returns the first element that pass a given test.
[findindex](../list/findindex) | Returns the index of the first element that pass a given test.
[indexof](../list/indexof) | Returns the index of a given value, or `nil` if not found.
[len](../list/len) | Returns the length of the tuple.
[map](../list/map) | Returns a new `list` with the results of calling a provided closure on every element.
[sort](../list/sort) | Returns a new sorted `list`.

{{% notice info %}}
The above methods correspond to those of a `list`. For that reason, they are only listed under the data type `list`.
{{% /notice %}}
