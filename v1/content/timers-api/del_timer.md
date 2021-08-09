---
title: "del_timer"
weight: 298
---

Delete a timer.

This function generates a [change](../../overview/changes).

### Function

`del_timer(timer)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
timer | int (required) | Timer Id to delete.

### Return value

Returns `nil` when successful. A [lookup_err()](../../errors/lookup_err) is raised if the timer does not exist.

### Example

> This code will will update `.counter` by one each minute.
> After 10 minutes the counter has reached 10 and will delete itself.

```thingsdb,should_pass

.counter = 0;

new_timer(
    datetime(),
    60,
    |timer| {
        .counter += 1;
        if (.counter == 10, {
            del_timer(timer);  // stop this timer
        });
    }
);

```
