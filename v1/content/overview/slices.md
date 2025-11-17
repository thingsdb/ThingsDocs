---
title: "Slices"
weight: 35
---

The following slice notation can be used:

```thingsdb,syntax_only
list[start:stop:step]
```

The `start` and `stop` value will default to `nil` and `step` has a default value of `1`.
For understanding slices it is important to remember that the `:stop` value represents the
first value that is *not* in the selected slice. This means that the
difference between `stop` and `start` is the number of selected items.
(assuming that `step` is the default value `1`)

Another feature is that *negative* numbers may be used. For `start` and `stop` this means that it
will count from the end of the array instead of the beginning.

> Some examples using `start` and `stop` to select some items:

```thingsdb,json_response
months = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December'];

[
    { months[:2];   /* first two months */ },
    { months[-2:];  /* last two months */ },
    { months[:-2];  /* all, except the last two months */ },
];
```

> ...and the corresponding result in JSON format:

```json
[
    [
        "January",
        "February"
    ],
    [
        "November",
        "December"
    ],
    [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October"
    ]
]
```

Another feature is the `step` argument, which also may be *negative* to reverse the
slice direction.

> Some examples using the `step` value:

```thingsdb,json_response
months = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December'];

[
    { months[::2];   /* only the odd months */ },
    { months[::-1];  /* months in reverse order, equal to months.reverse() */ },
];
```

> ...the corresponding result in JSON format:

```json
[
    [
        "January",
        "March",
        "May",
        "July",
        "September",
        "November"
    ],
    [
        "December",
        "November",
        "October",
        "September",
        "August",
        "July",
        "June",
        "May",
        "April",
        "March",
        "February",
        "January"
    ]
]
```

Slices can also be used to replace the [splice](../../data-types/list/splice) function.

{{% notice note %}}
It is not possible to use the `step` value when assigning items using the slice syntax.
{{% /notice %}}

> Example using the slice syntax to replace items in a list:

```thingsdb,json_response
months = ['January', 'February', 'XXX', 'May'];

/* Replace 'XXX' with 'March' and 'April' */
months[2:3] = ['March', 'April'];

/* Return result */
months;
```

> Once again the result in JSON format:

```json
[
    "January",
    "February",
    "March",
    "April",
    "May"
]
```

Instead of [lists](../../data-types/list) and [tuples](../../data-types/tuple) it also possible to use the slice notion on [strings](../../data-types/str)

> Slice on string example:

```thingsdb,json_response
/* Return 'abcdef' in reverse order */
"abcdef"[::-1];
```

```json
"fedcba"
```
