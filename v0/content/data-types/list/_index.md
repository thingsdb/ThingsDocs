---
title: "list"
weight: 800
---

An empty list can be constructed as follows: `list = [];`

Nesting is also possible withing but each nested list will become a [tuple](../tuple) which means the 'list' will be immutable.
ThingsDB does this because it wants to update all changes to subscribers and finds the subscribers by the parent object where
the change is  made. Since the parent of a nested 'list' is another list, the `thing` holding the list would not be found.

Another *weird* property of ThingsDB is that `lists` are always *copies*, and not by *reference* as in most languages. This is
because ThingsDB needs to know which subscribers to update with changes made to the `list`.

### Methods

Method | Description
------ | -----------
[extend](./extend) | Adds an array with items to the end of a list, and returns the new length.
[filter](./filter) | Returns a new `list` with elements that pass a given test.
[find](./find) | Returns the first element that pass a given test.
[findindex](./findindex) | Returns the index of the first element that pass a given test.
[indexof](./indexof) | Returns the index of a given value, or `nil` if not found.
[len](./len) | Returns the length of the list.
[map](./map) | Returns a new `list` with the results of calling a provided closure on every element.
[pop](./pop) | Removes the last element from an list and returns that element.
[push](./push) | Adds new items to the end of an list, and returns the new length.
[remove](./remove) | Removes the first element that pass a given test and returns that element.
[splice](./splice) | Determines if a string starts with characters given by another string.
[sort](./sort) | Returns a new sorted `list`.

{{% notice note %}}
It is not possible to change an list while the list is in use, for example: \
`tmp = [1, 2, 3]; tmp.map(|i| tmp.push(i));` \
...will raise `BAD_REQUEST` *(cannot change type `list` while the value is being used)*
{{% /notice %}}
