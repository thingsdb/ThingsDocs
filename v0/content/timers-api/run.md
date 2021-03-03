---
title: "run"
weight: 286
---

Run a timer.

{{% notice info %}}
The **run(..)** function may also be used to *run* a [procedure](../../procedures-api/run).
{{% /notice %}}

This function does *not* generate an [event](../../overview/events).

### Function

`run(timer)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
timer | int (required) | Id of the timer to run.

### Return value

Returns the timer response.

### Example

> Example code using *run*:

```thingsdb,json_response
.counter = 1;
timer = new_timer(datetime().move('days', 1), || .counter += 1);

wse(run(timer));
```

> Return value in JSON format

```json
2
```
