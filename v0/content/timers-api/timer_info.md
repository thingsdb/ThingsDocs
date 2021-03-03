---
title: "timer_info"
weight: 288
---

Returns information about a timer.

Value | Description
------- | -----------
`arguments` | Array with positional argument names.
`created_at` | [Time Stamp](https://wikipedia.org/wiki/Unix_time) when the timer is created.
`definition` | Closure definition. *(Only available with `EVENT` privileges)*
`doc` | Doc string of the closure in the timer.
`name` | Name of the timer.
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
new_timer('add_one', |x| {
    "Adds one to a given value";
    x + 1;
});

// Return the doc string for timer `add_one`
timer_info('add_one');
```

> Return value in JSON format

```json
{
    "arguments": [
        "x"
    ],
    "created_at": 1579175900,
    "definition": "|x| {\n    \"Adds one to a given value\";\n    x + 1;\n}",
    "doc": "Adds one to a given value",
    "name": "add_one",
    "with_side_effects": false
}
```
