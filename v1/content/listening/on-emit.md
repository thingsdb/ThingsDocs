---
title: "on-emit"
weight: 327
---

An emit event is triggered when a *change* is emitted using the [emit(..)](../../data-types/room/emit) function on a [room](../../data-types/room).

The event contains the room Id, a *change* name and arguments (`args`) as an array. If no arguments are attached to the event, `args` will be an empty array.

> Example *on-emit* event in JSON format:

```json
{
    "id": 123,
    "event": "my-event",
    "args": []
}
```

{{% notice note %}}
When using a *thing* as an argument, do not forget the default *deep* level is 1 and may required a higher value. (see the  [emit(..)](../../data-types/room/emit) function)
{{% /notice %}}