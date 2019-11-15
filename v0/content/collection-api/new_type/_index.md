---
title: "new_type"
date: 2019-10-23T16:58:46+02:00
weight: 28
---

Creates a new [Type](../../data-types/type).

This function generates an [event](../../events).

### Function

`new_type(type_name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type_name | string | Name of the Type to be created.

### Return value

The name of the newly created Type.

> This code shows the return value for ***new_type()***:

```thingsdb,json_response
new_type('NewType');
```

> Return value in JSON format

```json
"NewType"
```
