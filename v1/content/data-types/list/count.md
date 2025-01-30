---
title: "count"
weight: 73
---

Returns the number of times a value appears in a list. A [closure](../../closure) might be given which can be used as a shortcut for `.filter().len()`.

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`count(any)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
any | any | Element to count

### Return value

First item in the list.

### Example

> This code shows an example using ***count()***:

```thingsdb,json_response
[1, 4, 2, 9, 7, 8, 9, 3, 1].count(9);
```

> Return value in JSON format

```json
2
```

> Another example using a callback:

```thingsdb,json_response
// Count the values larger than 5
[1, 4, 2, 9, 7, 8, 9, 3, 1].count(|x| x > 5);
```

```json
4
```