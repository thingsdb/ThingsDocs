---
title: "each"
weight: 74
---

Iterate over all the items in an [list](../../list) or [tuple](../../tuple).
Use this functions instead of [map](../map) when you are *not* interested in the return value.

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`each(callback)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure (required) | Closure to execute on each value.

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
array    | item, index | Iterate over all items in the array. Both item and index are optional.

### Return value

None

### Example

> Generate the first `n` values of the Fibonacci sequence.

```thingsdb,json_response
fibonacci = |n| {
    seq = range(2);

    // Return the first `n` items when `n` is less or equal to 1.
    if (n <= 1) {
        return seq[:n];
    };

    // Append the sum of the last two items, and do this `n` minus 2 times.
    // Function `each` is used since we do not use the return value.
    range(2, n).each(||seq.push(seq[-2]+seq[-1]));

    // Return the sequence.
    seq;
};

// Return the first 10 items of the Fibonacci sequence.
fibonacci(10);
```

> Return value in JSON format

```json
[
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34
]
```
