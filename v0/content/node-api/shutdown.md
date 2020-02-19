---
title: "shutdown"
weight: 159
---

Shutdown the node in the selected scope. This is a clean shutdown, allowing all other nodes (and clients) to disconnect.

{{% notice warning %}}
At least **MODIFY** privileges on the `@node` scope are required to shutdown a node.
{{% /notice %}}

This function does *not* generate an [event](../../overview/events).

### Function

`shutdown();`

### Arguments

None.

### Return value

Returns `nil`.