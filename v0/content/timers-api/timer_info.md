---
title: "timer_info"
weight: 293
---

Returns information about a timer.

Value | Description
------- | -----------
`arguments` | Array with positional argument names.
`definition` | Closure definition. *(Only available with `EVENT` privileges)*
`doc` | Doc string of the closure in the timer.
`id` | Id of the timer.
`next_run` | Scheduled time when the timer wil run.
`repeat` | Repeat the timer each `X` seconds. *(Only when this is a repeating timer)*
`user` | User which credentials are used for the timer. *(Only available with `EVENT` privileges)*
`with_side_effects` | Boolean value which indicates if this timer has side effects.

This function does *not* generate an [event](../../overview/events).

### Function

`timer_info(timer)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`timer` | str (required) | Name of the timer where to return the info for.

### Return value

Returns [info](../../data-types/info) about a given timer.

### Example

> Create a new timer `add_one`:

```thingsdb,should_pass
timer = new_timer(
    datetime(),
    3600,
    || {
        "Remove disabled users each hour.";
        .users.remove(|user| user.disabled);
    }
);

timer_info(timer);
```

> Example return value in JSON format

```json
{
    "arguments": [],
    "definition": "|| {\n    \"Remove disabled users each hour.\";\n    .users.remove(|user| user.disabled);\n}",
    "doc": "Remove disabled users each hour.",
    "id": 9,
    "next_run": "2021-03-03 12:50:47Z",
    "repeat": 3600,
    "user": "admin",
    "with_side_effects": true
}
```
