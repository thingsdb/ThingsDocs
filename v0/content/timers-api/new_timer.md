---
title: "new_timer"
weight: 285
---

Creates a new timer to the `@thingsdb` or a `@collection` scope.
The given closure will be copied to the timer, so this is *not* a reference to the given closure.

This function generates an [event](../../overview/events).

### Function

`new_timer(start, [repeat], closure, [arguments])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`start` | datetime (required) | Time when the timer should start.
`repeat` | int (optional) | Repeat the timer each `X` seconds.
`closure` | closure (required) | Closure which will be attached to the timer.
`arguments` | array (optional) | Argument parsed to the closure.

### Return value

Returns the ID of the new timer.

