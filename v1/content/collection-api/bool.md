---
title: "bool"
weight: 205
---

Returns a [bool](../../data-types/bool) from a specified value.
If no value is given, `false` is returned.

Types with a *length* evaluate to `true` when the length is *not* `0`, and `false` otherwise.

This function does *not* generate a [change](../../overview/changes).

### Function

`bool(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (optional) | The value to convert to a boolean value.

### Return value

A boolean value.

### Example

> This code shows some return values for ***bool()***:

```thingsdb,json_response
[
    // Evaluate to false
    bool(),                       // default bool is false
    bool(0),                      // zero (0) evaluates to false
    bool(0.0),                    // zero float (0.0) evaluates to false
    bool(nil),                    // nil evaluates to false
    bool({}),                     // an empty thing evaluates to false
    bool(err()),                  // all errors evaluate to false
    bool(''),                     // an empty string evaluates to false
    bool([]),                     // an empty array evaluates to false
    bool(set()),                  // an empty set evaluates to false
    bool(room()),                 // a non-stored room (no Id) evaluates to false
    bool({
        t = task(datetime(), ||0);
        t.cancel();
        t;
    }),                            // non-scheduled tasks evaluate to false

    // Evaluate to true
    bool(42),                     // non zero integers evaluates to true
    bool(-1.0),                   // non zero float values evaluates to true
    bool({answer: 42}),           // non empty thing evaluates to true
    bool([1, 2, 3]),              // non empty array evaluates to true
    bool('forty two'),            // non empty string evaluates to true
    bool(set({}, {})),            // non empty set evaluates to true
    bool(.room = room()),         // a stored room (with Id) evaluates to true
    bool(future(||nil)),          // futures evaluate to true
    bool(timeval(0)),             // datetime and timeval always evaluate to true
    bool(task(datetime(), ||0)),  // scheduled tasks evaluate to true
];
```

> Return value in JSON format

```json
[
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    true,
    true,
    true,
    true,
    true,
    true,
    true,
    true,
    true,
    true
]
```
