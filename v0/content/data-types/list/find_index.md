---
title: "find_index"
weight: 65
---

This function returns the index of the first item in a [list](..) or [tuple](../../tuple) that passes the test.
Otherwise `nil` is returned.

This function does *not* generate an [event](../../../overview/events).

{{% notice warning %}}
This function has a deprecated alias `findindex` which will be removed in the next *minor* release.
{{% /notice %}}

### Function

*array*.`find_index(callback)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure | The statement to try.

Explanation of the *callback* argument:

Iterable | Callback arguments | Description
-------- | -------- | -----------
array | item, index | Iterate over items in the array. Both item and index are optional.

### Return value

The index of the first item in the array that passes the test;
otherwise, `nil` is returned.

### Example

> This code shows an example using ***find_index()***:

```thingsdb,json_response
// some sports as an example
sports = ['cycling', 'baseball', 'running', 'tennis', 'skateboarding'];

// return the index of `running` in list
sports.find_index(|sport| sport == 'running');
```

> Return value in JSON format

```json
2
```
