---
title: "del_type"
date: 2019-10-23T16:54:20+02:00
weight: 5
---

Deletes an existing type [Type](../../data-types/Type).

### Function

`del_type(type_name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type_name | string | Name of the Type to be deleted.

### Return value

The value `nil`.

> This code shows the return value for ***del_type()***:

```thingsdb,json_response
new_type('NewType');
del_type('NewType');
```

> Return value in JSON format

```json
null
```
