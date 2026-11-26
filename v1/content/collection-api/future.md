---
title: "future"
weight: 254
---

Returns a [future](../../data-types/future). It is *not* possible to assign or store a future in a `thing`, `dict`, `list`, or `tuple`; attempting to do so will raise a [type_err](../../errors/type_err).

{{% notice warning %}}
In versions before **v1.12.0**, assigning a `future` to a collection or adding it to a list did not raise an error and silently assigned `nil` instead.
{{% /notice %}}

If you want to use the return value from a future, you need to use [then(..)](../../data-types/future/then) and errors might be captured using the [else(..)](../../data-types/future/else) function.

A future's callback will get its own *change-Id* in case one is required. This means that it is possible to use a future to prevent a change in a query on some conditions (see last example).

This function does *not* generate a [change](../../overview/changes).

### Function

`future(request, arg1, arg2, ..., argX)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
request | thing/closure/nil (required) | The request or `nil` for a plain future. A `closure` can be used as a shortcut for `future(..).then(||...)`.
arg1..argX | any (optional) | Arguments which will be used in the *result*.

### Return value

A list with as first value the return value from the optional module or `nil` followed by the
future arguments.

### Example

> This code shows an example usage of  ***future()***:

```thingsdb,json_response
future(nil, 42);
```

> Return value in JSON format

```json
[null, 42]
```

> Use a future to prevent a change in some cases:

```thingsdb,should_pass
// dummy condition
condition = 2 > 1;

if (condition) future(|| {
    // a change is only required if the condition evaluates to `true`
    .only_if_condition = true;
});
```
