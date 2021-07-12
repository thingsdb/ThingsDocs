---
title: "future"
weight: 168
---

Returns a [future](../../data-types/future). It is *not* possible to assign a future to
a collection or add the future to a list. If you do, then `nil` will be assigned instead.

If you want to use the return value from a future, you need to use [then(..)](../../data-types/future/then) and

This function does *not* generate an [event](../../overview/events).

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
