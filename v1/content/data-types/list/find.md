---
title: "find"
weight: 81
---

This function returns the value of the first item in the [list](..) or [tuple](../../tuple) that passes the test.
Otherwise `nil` is returned  if no alternative return value is specified.

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`find(callback, [alt])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure | Closure to execute on each value until the closure evaluates to true.
alt | any (optional) | Alternative value which is returned if no item has passed the *callback* test.

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
array    | item, index | Iterate over items in the array. Both `item` and `index` are optional.

{{% notice note %}}
The `alt` argument will be *lazily* evaluated. Consider the following example: \
\
  `elems.find(|e| e.name == "foo", items.pop());` \
\
Here, the item will *only* be popped, in case `e` with `name` *foo* is *not* found in `elems`.
{{% /notice %}}

### Return value

The value of the first item in the array that passes the test;
otherwise, `nil` or a specified alternative value is returned.

### Example

> This code shows an example using ***find()***:

```thingsdb,syntax_only
users.find(|user| user.name.starts_with('Jeroen'));
```

> Example return value in JSON format

```json
{
    "#": 16,
    "email": "jeroen@cesbit.com",
    "name": "Jeroen van der Heijden"
}
```
