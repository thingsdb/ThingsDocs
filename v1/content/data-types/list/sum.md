---
title: "sum"
weight: 99
---

Returns the sum of each value in a list. A [closure](../../closure) might be given which can be used as a shortcut for `.map().sum()`.

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`sum([callback])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback  | closure (optional) | Use the callback on each element in the list and sum the return values.

### Return value

The sum of all values.

### Example

> This code shows an example using ***sum()***:

```thingsdb,json_response
[1, 4, 2, 9, 7, 8, 9, 3, 1].sum();
```

> Return value in JSON format

```json
44
```

> Another example using a callback:

```thingsdb,json_response
// Sum the x properties
[{x: 7, y: 1}, {x: 8, y: 5}].sum(|o| o.x);
```

```json
15
```