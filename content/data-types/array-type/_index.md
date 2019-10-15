---
title: "Array type"
date: 2019-10-14T09:41:11+02:00
weight: 1
---

An empty array can be constructed as follows: `arr = [];`

Nesting is also possible withing but each nested array will become a `tuple` which means the array will be immutable.
ThingsDB does this because it wants to update all changes to subscribers and finds the subscribers by the parent object where
the change is  made. Since the parent of a nested array is another array, the `thing` holding the array would not be found.

Another *weird* property of ThingsDB is that `arrays` are always *copies*, and not by *reference* as in most languages. This is
because ThingsDB needs to know which subscribers to update with changes made to the `array`.


### Methods
Method | Description
------ | -----------
[filter](../../collection-api/filter) | Returns a new `array` with elements that pass a given test.
[find](../../collection-api/find) | Returns the first element that pass a given test.
[findindex](../../collection-api/findindex) | Returns the index of the first element that pass a given test.
[indexof](../../collection-api/indexof) | Returns the index of a given value, or `nil` if not found.
[len](../../collection-api/len) | Returns the length of the array.
[map](../../collection-api/map) | Returns a new `array` with the results of calling a provided closure on every element.
[pop](../../collection-api/pop) | Removes the last element from an array and returns that element.
[push](../../collection-api/push) | Adds new items to the end of an array, and returns the new length.
[remove](../../collection-api/remove-list) | Removes the first element that pass a given test and returns that element.
[splice](../../collection-api/splice) | Determines if a string starts with characters given by another string.


### Array Types

Type | Description
---- | -----------
list | Mutable array.
tuple | Immutable array, *nested* arrays are always tuples.

{{% notice note %}}
It is not possible to change an array while the array is in use, for example: \
`tmp = [1, 2, 3]; tmp.map(|i| tmp.push(i));` \
...will raise `BAD_REQUEST` *(cannot change type `list` while the value is being used)*
{{% /notice %}}
