---
title: "return"
weight: 228
---

The `return` function moves the argument to the output of the current query/closure call.

If no `return` is specified, then the last value will be the value which is returned.
A second argument can be given to the return function which can be used to specify how `deep`
the result should be returned. The default `deep` value is set to 1, but any value between 0 and 127 is possible.
See the [deep](#deep) section for a detailed explanation of this argument.

A query can run different procedures and/or closures which might have changed the `deep` value. In case you
need to know the current `deep` value, the function [deep()](../../collection-api/deep) can be used.

{{% notice warning %}}
Be careful with using a deep value greater than one, especially when circular references are made since this can result
in returning a large amount of data.
{{% /notice %}}

When no arguments are used the return value will be `nil`.

This function does *not* generate a [change](../../overview/changes).

### Function

`return([value[, deep]])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (optional) | The value which will be moved to the output of the query or closure.
deep | int (optional) | Specify the `deep` value for the query (the current `deep` value will be overwritten).

### Return value

The `return` function has no real return value but will move directly
to the output of the current query or closure.

### Example

> This code shows how ***return()*** can be used:

```thingsdb,should_pass
// return .colors, two levels deep if .colors exists
try(return(.colors, 2));

// if .colors could not be returned, create the property
.colors = {
    aegean: {
        R: 0x5e,
        G: 0x8e,
        B: 0xc9,
    },
};

return(.colors, 2);
```

> Example return value in JSON format (the #ids might be different)

```json
{
    "#": 23,
    "aegean": {
        "#": 24,
        "B": 201,
        "G": 142,
        "R": 94
    }
}
```

### Deep

To understand the `deep` argument, suppose you have the following data:

```thingsdb,syntax_only
.artists = [{
    artist: "David Bowie",
    albums: [{
        name: "The Rise and Fall of Ziggy Stardust and the Spiders from Mars",
        songs: [{
            title: "Five Years",
            duration: 4.42
        }]
    }]
}];
```

If you only require the ID's from all `.artists` and do not any other properties, a value of `0` should be used for `deep`:

```thingsdb,syntax_only
return(.artists, 0);
```

Something like this will be returned. (the Id `#` might be different since this is auto generated)

```json
[
    {
        "#": 34580
    }
]
```

Here are some more examples using different values of *deep*:

> Return the artists, albums will be returned only with (#) ID's:

```thingsdb,syntax_only
.artists;  // Uses the default deep value of `1`
```

```json
[
    {
        "#": 34580,
        "albums": [
            {
                "#": 34581
            }
        ],
        "artist": "David Bowie"
    }
]
```

> Return the artists and albums, songs will be returned only with (#) ID's:

```thingsdb,syntax_only
return(.artists, 2);
```

```json
[
    {
        "#": 34580,
        "albums": [
            {
                "#": 34581,
                "name": "The Rise and Fall of Ziggy Stardust and the Spiders from Mars",
                "songs": [
                    {
                        "#": 34582
                    }
                ]
            }
        ],
        "artist": "David Bowie"
    }
]
```

> Return the artists, albums and songs:

```thingsdb,syntax_only
return(.artists, 3);
```

```json
[
    {
        "#": 34580,
        "albums": [
            {
                "#": 34581,
                "name": "The Rise and Fall of Ziggy Stardust and the Spiders from Mars",
                "songs": [
                    {
                        "#": 34582,
                        "duration": 4.42,
                        "title": "Five Years"
                    }
                ]
            }
        ],
        "artist": "David Bowie"
    }
]
```

{{% notice tip %}}
Use custom [Type](../../data-types/type) and the [wrap()](../../data-types/thing/wrap) function to gain more control on which properties to return.
{{% /notice %}}

