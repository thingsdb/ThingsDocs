---
title: "tuple"
weight: 138
---

All nested *arrays* are immutable and thus tuples.

```thingsdb,should_pass
list = [];
list.push(['this list will be nested and therefore convert to a tuple']);

// Check that the first item in `list` is indeed a `tuple`
assert(is_tuple(list[0]));

// Check that the `tuple` is indeed immutable
assert(is_err(try(list[0].push('cannot be added to a tuple'))));
```

A `tuple` only becomes a `tuple` when it is nested inside another `tuple` or `list`, which means the `tuple` will be immutable.
ThingsDB does this to make watching things possible; it wants to update all changes within a thing to the subscribers that are watching, and finds them by thing. Since the parent of a nested `tuple` is another `tuple` or `list`, the watched `thing` holding the `list`with nested lists would not be found.

Another property of `lists` and `tuples` in ThingsDB is that they both are always *copies*, and not a *reference* as in most languages. This is also done to enable watching.

### Functions

Function | Description
------ | -----------
[choice](../list/choice) | Return a random item from a tuple.
[each](../list/each) | Iterate over all items in a tuple.
[every](../list/every) | Check if all items pass a given test.
[filter](../list/filter) | Return a new `list` with items that pass a given test.
[find](../list/find) | Return the first item that pass a given test.
[find_index](../list/find_index) | Return the index of the first item that pass a given test.
[first](../list/first) | Return the first item from a tuple.
[has](../list/has) | Return `true` if a given value is found in the tuple, or `false` if not found.
[index_of](../list/index_of) | Return the index of a given value, or `nil` if not found.
[is_unique](../list//is_unique) | Returns `true` if each item in a tuple is unique or `false` if a duplicate is found.
[join](../list/join) | Returns a string with all items joined.
[last](../list/last) | Return the last item from a tuple.
[len](../list/len) | Return the length of the tuple.
[map](../list/map) | Return a new `list` with the results of calling a provided closure on every item.
[reduce](../list/reduce) | Execute a reducer function on each item, resulting in a single output value.
[reverse](../list/reverse) | Return a new list with the items in reverse order.
[some](../list/some) | Check if at least one item passes a given test.
[sort](../list/sort) | Return a new sorted `list`.
[unique](../list/unique) | Returns a new list without duplicate items.

{{% notice info %}}
The above functions correspond to those of a `list`. For that reason, they are only listed under the data type `list`.
{{% /notice %}}
