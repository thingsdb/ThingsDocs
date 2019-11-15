---
title: "del"
date: 2019-10-23T13:53:55+02:00
weight: 1
---

Delete a property from a [thing](..).

This function generates an [event](../../../events).

### Function

*thing*.`del(property)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
property | str (required) | Name of the property to delete.

### Return value

Returns `nil` if successful. An `INDEX_ERROR` is returned
if the property does not exist or `BAD_REQUEST` in case the given property is
not a valid [name](../../../names).

> This code shows some return values for ***del()***:

```thingsdb,json_response
.x = 'create and delete this prop';
.del('x');
```

> Return value in JSON format

```json
null
```