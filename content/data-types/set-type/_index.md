---
title: "Set type"
date: 2019-10-14T09:41:39+02:00
weight: 9
---

A set is a collection which is unordered and can only contain things.
Each [thing](../../thingsdb-api) will only exists once in a collection.

### Methods
Method | Description
------ | -----------
[add](../../collection-api/add) | Add things to a set.
[filter](../../collection-api/filter) | Return a new `set` with things that pass a given test.
[find](../../collection-api/find) | Returns the first `thing` which passes a given test.
[has](../../collection-api/has-set) | Test if a set contains a given thing.
[map](../../collection-api/map) | Return an [array](../../data-types/array-type) with the results of calling a provided closure on every thing.
[remove](../../collection-api/remove-set) | Remove things from a set.
[set](../../data-types/set) | Create a new empty set or convert an [array](../../data-types/array-type) to a new set.
