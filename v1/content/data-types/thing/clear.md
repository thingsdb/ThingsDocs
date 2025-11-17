---
title: "clear"
weight: 169
---

Removes all properties from a [thing](..).

This function generates a [change](../../../overview/changes)

### Function

*thing*.`clear()`

### Arguments

None

### Return value

Returns `nil`.

### Example

> This code adds things to a set:

```thingsdb,json_response
my_thing = {
    a: 'Property A',
    b: 'Property B',
    c: 'Property C'
};

my_thing.clear();
my_thing;  // the thing is empty
```

> Return value in JSON format

```json
{}
```
