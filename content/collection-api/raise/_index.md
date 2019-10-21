---
title: "raise"
date: 2019-10-14T10:03:58+02:00
weight: 45
---

Raises an [error](../../data-types/error-type).

This function does *not* generate an [event](../../events).

### Function
`raise([error])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | error (optional) | The error to raise.

### Return value
None

> This code shows how ***raise()*** can be used:

```thingsdb,should_err
raise ();
'This code is not reached';
```
