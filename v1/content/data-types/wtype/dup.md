---
title: "dup"
weight: 172
---

Duplicate a [wrapped](../) thing.

{{% notice warning %}}
The function preserves both the wrap and Type of a thing. Use [copy(..)](../copy) if you want a new plain thing.
{{% /notice %}}

This function does *not* generate a [change](../../../overview/changes).

### Function

*`<Type>`*.`dup([deep]])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
deep | int (optional) | How *deep* to duplicate the *wrapped* thing. Default is `1`.

### Return value

A new *wrapped* thing.

### Example

> This code shows an example using ***dup()*** on a wrapped thing:

```thingsdb,json_response
set_type('Person', {
    name: 'str'
});

robot = {
    name: 'Foo',
    isHuman: false
};

foo = robot.wrap('Person').dup();

foo.unwrap();  // foo is still wrapped, the underlying `robot` is being duplicated.
```

> Return value in JSON format

```json
{
    "name": "Foo",
    "isHuman": false
}
```


