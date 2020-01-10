---
title: "del"
weight: 67
---

Delete a property from a [thing](..).

This function generates an [event](../../../overview/events).

### Function

*thing*.`del(property)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
property | str (required) | Name of the property to delete.

### Return value

Returns `nil` if successful. A [lookup_err()](../../errors/lookup_err) is returned
if the property does not exist or [bad_data_err()](../../errors/bad_data_err) in case the given property is
not a valid [name](../../../overview/names).

### Example

> This code shows some return values for ***del()***:

```thingsdb,json_response
.x = 'create and delete this prop';
.del('x');
```

> Return value in JSON format

```json
null
```
