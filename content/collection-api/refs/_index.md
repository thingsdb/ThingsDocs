---
title: "refs"
date: 2019-10-14T10:04:02+02:00
weight: 31
---

Returns the reference count of a value.

The count returned is generally one higher than you might expect,
because it includes the (temporary) reference.

{{% notice note %}}
Different nodes might return different reference values since the reference counter
can be higher of lower depending on how the value is stored and used.
{{% /notice %}}

This function does *not* generate an [event](../../events).

### Function

`refs(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to return the reference count for.

### Return value

Reference count of the given value.

> Returns the reference count of a given value:

```thingsdb,should_pass
[
    refs( 'some string' ),
    refs( a = b = c = 42 ),
];
```

> Example return value in JSON format

```json
[
    2,
    5
]
```
