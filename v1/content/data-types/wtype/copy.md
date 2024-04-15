---
title: "copy"
weight: 189
---

Copy a [wrapped](../) thing.

{{% notice warning %}}
The function does *not* preserve the *wrap* or *Type* of a thing. Use [dup(..)](../dup) if you want a true duplicate.
{{% /notice %}}

This function does *not* generate a [change](../../../overview/changes).

### Function

*`<Type>`*.`copy([deep]])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
deep | int (optional) | How *deep* to copy the *wrapped* thing. Default is `1`.

### Return value

A new thing.

### Example

> This code shows an example using ***copy()*** on a wrapped thing:

```thingsdb,json_response
set_type('Person', {
    name: 'str'
});

robot = {
    name: 'Foo',
    isHuman: false
};

foo = robot.wrap('Person').copy();

foo;  // note that only `name` is copied
```

> Return value in JSON format

```json
{
    "name": "Foo"
}
```


