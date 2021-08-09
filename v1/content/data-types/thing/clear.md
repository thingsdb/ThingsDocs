---
title: "clear"
weight: 123
---

Removes all properties from a [thing](..).

This function generates a [change](../../../overview/changes) *(except when called on a [variable](../../../overview/variable))*.

### Function

*thing*.`clear()`

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
