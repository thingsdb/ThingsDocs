---
title: "raise"
date: 2019-10-14T10:03:58+02:00
weight: 3000
---

Raises an [error](../../data-types/error).

This function does *not* generate an [event](../../events).

### Function

`raise([error])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | error/str (optional) | The error to raise.

### Return value

None

> Some examples on how ***raise()*** can be used:

```thingsdb,should_err
raise ();  // raise a default error
'This code is not reached';
```

```thingsdb,should_err
raise ('no licenses left');  // raise with a custom message
'This code is not reached';
```

```thingsdb,should_err
raise (value_err());  // raise a value error
'This code is not reached';
```
