---
title: "findindex"
weight: 34
---

This function returns the index of the first element in a [list](..) or [tuple](../../tuple) that satisfies the callback function.
Otherwise `nil` is returned.

This function does *not* generate an [event](../../../overview/events).

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

The index of the first element in the array that satisfies the provided testing function;
otherwise, `nil` is returned.

### Example

> This code shows an example using ***findindex()***:

```thingsdb,json_response
// some sports as an example
sports = ['cycling', 'baseball', 'running', 'tennis', 'skateboarding'];

// return the index of `running` in list
sports.findindex(|sport| sport == 'running');
```

> Return value in JSON format

```json
2
```
