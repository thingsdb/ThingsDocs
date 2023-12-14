---
title: "on-emit"
weight: 369
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
When using a *thing* in the argument(s), do not forget to check the  *deep* value. (see the [emit(..)](../../data-types/room/emit) function)
{{% /notice %}}