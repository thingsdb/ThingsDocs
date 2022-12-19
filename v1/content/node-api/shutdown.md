---
title: "shutdown"
weight: 303
---

Shutdown the node in the selected scope. This is a clean shutdown, allowing all other nodes (and clients) to disconnect.

{{% notice warning %}}
At least **CHANGE** privileges on the `@node` scope are required to shutdown a node.
{{% /notice %}}

This function does *not* generate a [change](../../overview/changes).

### Function

`shutdown()`

### Arguments

None.

### Return value

Returns `nil`.
