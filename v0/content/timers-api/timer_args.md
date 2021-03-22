---
title: "timer_args"
weight: 292
---

Get timer arguments as a [tuple](../../data-types/tuple).

{{% notice info %}}
The first argument for a timer closure is the *timer_id*. This `timer_id` is *not* included
in the list of arguments.
{{% /notice %}}

This function does *not* generate an [event](../../overview/events).

### Function

`timer_args(timer)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
timer | int (required) | Timer to get the arguments for.

### Return value

Returns a `tuple` with arguments.

### Example

> This code will will be called every minute for 10 times and then it the timer will be removed.

```thingsdb,should_pass

timer = new_timer(
    datetime().move('days', 1),
    |timer, a, b| {
        .sum = a + b;
    },
    [4, 6]
);

timer_args(timer);
```
