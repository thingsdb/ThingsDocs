---
title: "flat"
weight: 81
---

The function returns a new `list` with all `tuple` elements concatenated into it recursively up to a specified depth.

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`flat([depth])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
depth    | int (optional) | The depth level specifying how deep a nested structure should be flattened _(Defaults to `1`)_.

### Return value

A new `list` with all `tuple` elements concatenated into it recursively up to a specified depth.

### Example

> Using flat with default depth _(1)_:

```thingsdb,json_response
[1, [2], [3, 4, [5, 6]]].flat();
```

> Return value in JSON format

```json
[1, 2, 3, 4, [5, 6]]
```

> Using flat with default specified depth _(2)_:

```thingsdb,json_response
[1, [2], [3, 4, [5, 6]]].flat(2);
```

> Return value in JSON format

```json
[1, 2, 3, 4, 5, 6]
```
