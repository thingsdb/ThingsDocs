---
title: "first"
weight: 79
---

Returns the first item in the list. A [lookup_err()](../../../errors/lookup_err) is raised when this function is used on an empty list unless a default value is given, in which case the given value will be returned.

{{% notice note %}}
ThingsDB uses *lazy-evaluation* of function arguments. For this reason the default value might be a function call or code block which will only be evaluated when the list is *empty*.
{{% /notice %}}

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`first([alt]])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
alt | any (optional) | Alternative value which is returned when the list is empty.

### Return value

First item in the list.

### Example

> This code shows an example using ***first()***:

```thingsdb,json_response
["January", "February", "March", "April"].first();
```

> Return value in JSON format

```json
"January"
```

