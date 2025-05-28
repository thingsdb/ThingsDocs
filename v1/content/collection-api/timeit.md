---
title: "timeit"
weight: 319
---

The _timeit_ function can be used to check the duration of some code. It only measures the execution time of the code and does not include additional change creation and does not wait for futures to be completed.
The function accepts any code and returns with a new thing with two properties:

* _time_ : A float value representing the execution time in seconds.
* _data_ : The return value for the code.


It is _(almost)_ a shortcut for the following ThingsDB code:

```thingsdb,should_pass
_timeit = |code| {
    start = now();
    data = code();
    time = now() - start;
    {
        time:,
        data:,
    };
 };

 // example usage:
 _timeit(|| {
    // code to time
    2 + 2;
 });
```

This function does *not* generate a [change](../../overview/changes).

### Return value

Returns a [thing](../../data-types/thing) with a _time_ and _data_ property.

### Example

> This code shows an example for ***timeit()***:

```thingsdb,should_pass
timeit({
    range(1, 11).map(|x| `{x} x 7 = {x*7}`);  // generates table of seven
});
```

> Example return value:

```json
{
    "data": [
        "1 x 7 = 7",
        "2 x 7 = 14",
        "3 x 7 = 21",
        "4 x 7 = 28",
        "5 x 7 = 35",
        "6 x 7 = 42",
        "7 x 7 = 49",
        "8 x 7 = 56",
        "9 x 7 = 63",
        "10 x 7 = 70"
    ],
    "time": 0.000057546
}
```
