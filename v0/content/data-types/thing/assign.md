---
title: "assign"
weight: 109
---

Copies properties from a given [thing](..). Existing properties will be overwritten and new properties will be added. If this function is used on an instance of a custom [Type](../../type), *all* properties of the source must be valid according the type specification, otherwise an exception will be raised and no properties will be copied.

This function generates an [event](../../../overview/events).

### Function

*thing*.`assign(source)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
source | thing (required) | Thing from which the properties are copied.

### Return value

Returns the `thing` to which the properties are assigned.

### Example

> This code shows an example using ***assign()***:

```thingsdb,json_response
scores = {
    iris: 10,
    job: 20
};

scores.assign({
    job: 80,
    tijs: 90
});
```

> Return value in JSON format

```json
{
    "iris": 10,
    "job": 80,
    "tijs": 90
}
```
