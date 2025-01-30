---
title: "closure"
weight: 213
---

Returns an [closure](../../data-types/closure) from a given string.
If no value is given, the default closure `|| nil` is returned.

This function does *not* generate a [change](../../overview/changes).

### Function

`closure(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | str (optional) | Convert a string into a closure. If omitted the default closure `\|\| nil` is returned.

### Return value

An new closure.

### Example

> This code shows some return values for ***closure()***:

```thingsdb,json_response
s = '|x| x*2';
c = closure(s);
c(21);
```

> Return value in JSON format

```json
42
```
