---
title: "tuple"
date: 2019-10-23T11:04:51+02:00
weight: 14
---

An empty tuple can be constructed as follows:

```thingsdb,should_pass
list = [];
tuple = [];
list.push(tuple);
```

A tuple only becomes a `tuple` when it is nested inside a list, which means the 'list' will be immutable.
ThingsDB does this because it wants to update all changes to subscribers and finds the subscribers by the parent object where
the change is  made. Since the parent of a nested 'list' is another list, the `thing` holding the list would not be found.

Another *weird* property of ThingsDB is that `tuples` are always *copies*, and not by *reference* as in most languages. This is
because ThingsDB needs to know which subscribers to update with changes made to the `tuple`.

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
