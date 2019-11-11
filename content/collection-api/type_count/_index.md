---
title: "type_count"
date: 2019-10-23T16:59:23+02:00
weight: 39
---

Returns the number of instances of a given [Type](../../data-types/type) within a collection.

This function does *not* generate an [event](../../events).

### Function

`type_count(type_name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type_name | str | The name of the Type for which the number of instances must be returned.

### Return value

An `int` representing the number of occurrences.
