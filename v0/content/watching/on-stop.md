---
title: "on-stop"
weight: 232
---

A stop event will be pushed as soon as a [thing](../../data-types/thing) is no longer being watched.

{{% notice warning %}}
This event is not pushed when a connection to a node is lost but only when watching is stopped by the user.
{{% /notice %}}

> Example *watch stop* event in JSON format:

```json
{
    "#": 42
}
```
