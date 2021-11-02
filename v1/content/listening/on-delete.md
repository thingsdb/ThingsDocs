---
title: "on-delete"
weight: 328
---

A delete event will be pushed as soon as a joined [room](../../data-types/room) is removed from ThingsDB.

{{% notice warning %}}
If this event is not received when expected, the reason might be that the `room` belonged to a thing that had a circular reference.
In this case you have to wait until **garbage collection** has cleaned the *thing* from ThingsDB. This is done when the node is in *away* mode.
{{% /notice %}}

> Example *on-delete* event in JSON format:

```json
{
    "id": 42
}
```
