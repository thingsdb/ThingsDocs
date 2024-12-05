---
title: "is_unique"
weight: 86
---

This function determines whether each item in a list is unique or not.

An item in the list is marked as a duplicate when an item is compared as equal to another item using the `==` operator.

This function does *not* generate a [change](../../../overview/changes).

### Function

*list*.`is_unique()`


### Arguments

None

### Return value

Returns `true` if each item in the list is unique or `false` if not.

### Example

> This code shows some return values for ***is_unique()***:

```thingsdb,json_response
[
    ["a", "b", "c"].is_unique(),
    ["foo", "bar", "foo"].is_unique(),
];
```

> Return value in JSON format

```json
[
    true,
    false
]
```
