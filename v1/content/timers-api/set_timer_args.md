---
title: "set_timer_args"
weight: 304
---

Set timer arguments.

If less than the required arguments are given, then the remaining arguments will
be set using `nil`. More arguments than the closure accepts are simply removed and thus not used.

{{% notice warning %}}
When the timer is created in the `@thingsdb` scope, only type `nil`, `int`, `float`, `bool`, `str`, `bytes`, `datetime` and `regex` are allowed as argument values.
{{% /notice %}}

This function generates a [change](../../overview/changes).

### Function

`set_timer_args(timer, args)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
timer | int (required) | Timer to set new arguments for.
args | list (required) | List with timer arguments.

### Return value

Returns `nil` when successful. A [lookup_err()](../../errors/lookup_err) is raised if the timer does not exist.

### Example

> This code will will be called every minute for 10 times and then it the timer will be removed.

```thingsdb,should_pass

new_timer(
    datetime(),
    60,
    |timer, x| {
        set_timer_args(timer, [x+1]);
        if (x == 10, {
            del_timer(timer);  // stop this timer
        });
    },
    [1]
);

```
