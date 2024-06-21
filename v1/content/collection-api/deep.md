---
title: "deep"
weight: 211
---

Set or return the current `deep` value for the **running query**. The deep value indicates how far down the result of a query is returned. For example, *thing1* may contain a *thing2* that contains a *thing3*. A deep value of 1 would only show the content of *thing1* and a deep value of 3 will go as deep as the content of *thing3*. ThingsDB allows *deep* to have a value between `0` and `127`.

Besides this function the `deep` value can change after a closure with a [return](../../overview/statements/#return) statement has changed the `deep` value for this query.

This function does *not* generate a [change](../../overview/changes).

### Function

`deep([deep])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
deep | int (optional) | Set a new *"deep"* level. If not given, the current deep level is returned.

### Return value

The current `deep` value for the running query.

### Example

> This code uses `deep()` to set *deep* to a new value:

```thingsdb,json_response
deep(3);  // Set the `deep` value to 3 for this query
{
    v: "Level 1",
    a: {
        v: "Level 2",
        b: {
            v: "Level 3",
            c: {
                v: 'Level 4'
            }
        }
    }
};
```

> Return value in JSON format *(c, level 4, is not included as we use deep 3)*

```json
{
    "a": {
        "b": {
            "c": {},
            "v": "Level 3"
        },
        "v": "Level 2"
    },
    "v": "Level 1"
}
```
