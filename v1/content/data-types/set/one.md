---
title: "one"
weight: 119
---

This function returns a _thing_ from a [set](..). The set must contain at least one
thing, otherwise a [lookup_err()](../../../errors/lookup_err) is raised.

{{% notice warning %}}
The _thing_ which is returned from the _set_ is neither random nor predictable.
{{% /notice %}}

This function does *not* generate a [change](../../../overview/changes).

### Function

*set*.`one()`

### Arguments

None

### Return value

One _thing_ from the _set_ or a [lookup_err()](../../../errors/lookup_err) when empty.

### Example

> This code shows an example using ***one()***:

```thingsdb,should_pass
// Returns either Iris, Cato or Tess
set({name: 'Iris'},
    {name: 'Cato'},
    {name: 'Tess'},
).one();
```

> Example return value in JSON format

```json
{
    "name": "Iris"
}
```
