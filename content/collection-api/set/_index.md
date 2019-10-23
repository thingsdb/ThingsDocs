---
title: "set"
date: 2019-10-14T10:04:55+02:00
weight: 50
---

Returns a new empty [set](../../data-types/set). If an array is given, then all elements in the
given array must be or type `thing` and a new set is returned based on the
given things. Instead of an array, it is also possible to provide things comma separated.

This function does *not* generate an [event](../../events).

### Function
`set(array_or_things)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
array_or_things | array/things (optional) | Optional array or things to initialize the set.

### Return value
A new set.

> This code shows some return values for ***set()***:

```thingsdb,json_response
set({name: 'Iris'});
```

> Return value in JSON format

```json
{
    "$": [
        {
            "name": "Iris"
        }
    ]
}
```
