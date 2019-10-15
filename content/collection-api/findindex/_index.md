---
title: "findindex"
date: 2019-10-14T09:59:22+02:00
weight: 14
---

This function returns the index of the first element in an [array](../../data-types/array-type) that satisfies the callback function.
Otherwise `nil` is returned.

This function does *not* generate an [event](../../events).

### Function
*array*.`findindex(callback)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
callback | closure | The statement to try.

Explanation of the *callback* argument:

Iterable | Callback arguments | Description
-------- | -------- | -----------
array | item, index | Iterate over items in the array. Both item and index are optional.


### Return value
The index of the first element in the array or thing that satisfies the provided testing function;
otherwise, `nil` is returned.

> This code shows an example using ***findindex()***:

```
users.findindex(|user| user.name.startswith('Jeroen'));
```

> Example return value in JSON format

```json
42
```
