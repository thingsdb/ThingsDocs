---
title: "on-init"
weight: 279
---

This event will be pushed on every request to watch a [thing](../../data-types/thing).

> Example *on-init* event in JSON format:

```json
{
    "event": 123,
    "collection": "stuff",
    "thing": {
        "#": 42,
        "name": "Iris"
    }
}
```

If the [thing](../../data-types/thing) *IS* actually a collection, then the *init* event also contains all [types](../../data-types/type) and [procedures](../../procedures-api) inside the collection.

> Example *on-init* event for a collection in JSON format:

```json
{
    "event": 123,
    "collection": "stuff",
    "thing": {
        "#": 3
    },
    "types": [
        {
            "type_id": 1,
            "name": "Sample",
            "created_at": 1579592122,
            "modified_at": 1579592122,
            "fields": [
                ["name", "str?"]
            ],
            "methods": {},
            "wrap_only": false
        }
    ],
    "procedures": [
        {
            "doc": "Sample procedure",
            "name": "multiply",
            "created_at": 1579592122,
            "definition": "|a,b|{'Sample procedure';a*b;}",
            "with_side_effects": false,
            "arguments": ["a", "b"]
        }
    ]
}
```
