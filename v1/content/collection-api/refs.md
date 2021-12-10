---
title: "refs"
weight: 248
---

Returns the reference count of a value.

Generally, the count returned is one higher than you might expect,
because it includes the (temporary) reference.

{{% notice info %}}
Different nodes might return different reference values since the reference counter
can be higher or lower depending on how the value is stored and used.
{{% /notice %}}

This function does *not* generate a [change](../../overview/changes).

### Function

`refs(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to return the reference count for.

### Return value

Reference count of the given value.

### Example

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
