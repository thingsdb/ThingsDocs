---
title: "list"
weight: 35
---

An empty list can be constructed as follows: `list = [];`

Nesting is also possible withing but each nested list will become a [tuple](../tuple) which means the 'list' will be immutable.
ThingsDB does this because it wants to update all changes to subscribers and finds the subscribers by the parent object where
the change is  made. Since the parent of a nested 'list' is another list, the `thing` holding the list would not be found.


### Methods

Method | Description
------ | -----------
[choice](./choice) | Returns a random item from a list.
[each](./each) | Iterate over all items in a list.
[every](./every) | Test whether all elements pass a given test.
[extend](./extend) | Adds an array with items to the end of a list, and returns the new length.
[filter](./filter) | Returns a new `list` with elements that pass a given test.
[find](./find) | Returns the first element that pass a given test.
[findindex](./findindex) | Returns the index of the first element that pass a given test.
[indexof](./indexof) | Returns the index of a given value, or `nil` if not found.
[len](./len) | Returns the length of the list.
[map](./map) | Returns a new `list` with the results of calling a provided closure on every element.
[pop](./pop) | Removes the last element from an list and returns that element.
[push](./push) | Adds new items to the end of an list, and returns the new length.
[reduce](./reduce) | Executes a reducer function on each element, resulting in a single output value.
[remove](./remove) | Removes the first element that pass a given test and returns that element.
[some](./some) | Test whether at least one element passes a given test.
[sort](./sort) | Returns a new sorted `list`.
[splice](./splice) | Determines if a string starts with characters given by another string.

{{% notice note %}}
It is not possible to change an list while the list is in use, for example: \
`tmp = [1, 2, 3]; tmp.map(|i| tmp.push(i));` \
...will raise [bad_data_err()](../../errors/bad_data_err) *(cannot change type `list` while the value is being used)*
{{% /notice %}}


### Reference versus copy

It might be useful to understand when ThingsDB uses a *reference* to a `list`, and when it makes *copy*. As long as a `list`
is used as a [variable](../../overview/variable), then ThingsDB uses a *reference* to the list. If a `list` will be assigned
to a [thing](../thing), or if a `list` which *is* assigned to a [thing](../thing), will be assigned to a [variable](../../overview/variable), then a *copy* will be made.
For example:

```thingsdb,json_response
a = [1, 2];
b = a;  // both `a` and `b` are variable so a *reference* is used.
.c = a;  // `c` is assigned, so a *copy* will be made.
a.push(3);  // note that `.c` is not affected because `.c` is a *copy*.

// Return the values
[a, b, .c];
```
> Response in JSON format:

```json
[
    [1, 2, 3],
    [1, 2, 3],
    [1, 2]
]
```

The same is true for when a `list` is used within a closure. For example:

```thingsdb,should_pass
a = [];    // `list` assigned to a variable

// `a` stays a variable, so a reference will be used
a2 = range(3).reduce(|arr, val| {arr.push(val); arr;}, a);   // [0, 1, 2]

assert (a == a2);   // both `a` and `a2` are a reference to the same list
```

> And when a `list` is assigned to a thing...

```thingsdb,should_pass
.b = [];   // `list` assigned to a thing

// `.b` will be assigned to `arr`, so in the first iteration a *copy* will be made
b2 = range(3).reduce(|arr, val| {arr.push(val); arr;}, .b);  // [0, 1, 2]

assert (.b != b2);  // [] != [0, 1, 2]
```