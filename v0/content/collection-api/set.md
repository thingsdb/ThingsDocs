---
title: "set"
weight: 206
---

Returns a new empty [set](../../data-types/set). If an array is given, then all items in the
given array must be of type `thing` and a new set is returned based on the
given things. Instead of an array, it is also possible to provide one thing or multiple comma-separated things.

This function does *not* generate an [event](../../overview/events).

### Function

`set(array_or_things)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
array_or_things | array/things (optional) | Optional array or things to initialize the set.

### Return value

A new set.

### Example

> This code shows some return values for ***set()***:

```thingsdb,json_response
set({name: 'Iris'});
```

> Return value in JSON format

```json
[
    {
        "name": "Iris"
    }
]
```
