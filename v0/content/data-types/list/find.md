---
title: "find"
date: 2019-10-23T12:51:28+02:00
weight: 3
---

This function returns the value of the first element in the [list](..) or [tuple](../../tuple) that satisfies the callback function.
Otherwise `nil` is returned unless an alternative return value is specified.

This function does *not* generate an [event](../../../events).

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
The `alt` argument will be *lazy* evaluated. Consider the following example: \
`elems.find(|e| (e.name == "foo"), items.pop());` \
Here, the item will *only* be popped, in case `e` with `name` *foo* is *not* found in `elems`.
{{% /notice %}}

### Return value

The value of the first element in the array that satisfies the provided testing function;
otherwise, `nil` or a specified alternative value is returned.

> This code shows an example using ***find()***:

```thingsdb,syntax_only
users.find(|user| user.name.startswith('Jeroen'));
```

> Example return value in JSON format

```json
{
    "#": 16,
    "email": "jeroen@transceptor.technology",
    "name": "Jeroen van der Heijden"
}
```