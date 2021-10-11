---
title: "new_timer"
weight: 304
---

Creates a new timer to the `@thingsdb` or a `@collection` scope.
The given closure will be copied to the timer, so this is *not* a reference to the given closure.

{{% notice warning %}}
When the timer is created in the `@thingsdb` scope, only type `nil`, `int`, `float`, `bool`, `str`, `bytes`, `datetime` and `regex` are allowed as argument values.
{{% /notice %}}

This function generates a [change](../../overview/changes).

### Function

`new_timer(start, [repeat], closure, [arguments])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`start` | datetime (required) | Time when the timer should start.
`repeat` | int/nil (optional) | Repeat the timer each `X` seconds. Value `nil` will disable `repeat` and will fire the timer only once. The *minimal* repeat value is `30` seconds.
`closure` | closure (required) | Closure which will be attached to the timer.
`arguments` | array (optional) | Argument parsed to the closure.

### Return value

Returns the Id of the new timer.

