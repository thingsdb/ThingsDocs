---
title: "on-delete"
weight: 235
---

A delete event will be pushed as soon as a [thing](../../data-types/thing) which you are watching, is removed from ThingsDB.

{{% notice warning %}}
If this event is not received when expected, there might exist circular references to the removed *thing*.
In this case you have to wait until **garbage collection** has cleaned the *thing* from ThingsDB. This is done when the node is in *away* mode.
{{% /notice %}}

> Example *watch delete* event in JSON format:

```json
{
    "#": 42
}
```
