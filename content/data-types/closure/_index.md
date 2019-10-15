---
title: "Closure"
date: 2019-10-14T09:41:26+02:00
weight: 3
---

Closures can be used to consume items from a `thing`, `array` or `set`.

{{% notice note %}}
It is not possible to use closures with recursion, for example: \
`a = ||map(a); map(a);` \
...will raise `BAD_REQUEST` *(closures cannot be used recursively)*
{{% /notice %}}
