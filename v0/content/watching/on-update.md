---
title: "on-update"
weight: 191
---

An update event is pushed when changed are made to a `thing` you are watching.
Nested things need to be watched separate.

The event contains the Thing ID (`#`), an event number, and an *jobs* array containing all the mutations which are applied to the thing in the order as they are put in the array.

```json
{
    "#": 3,
    "event": 123,
    "jobs": [
        ...
    ]
}
```

Each mutation is a *map* `{}` with a single *key*. This key tells what kind of *mutation* is applied to the thing.

Mutation | Target | Description
-------- | ------ | -----------
[set](#set) | `thing` | Add a new property.
[del](#del) | `thing` | Delete a property.
[add](#add) | `thing` | Add one or more [things](../../data-types/thing) to a [set](../../data-types/set).
[remove](#remove) | `thing` | Remove one or more [things](../../data-types/thing) from a [set](../../data-types/set).
[splice](#splice) | `thing` | Delete and/or add items to a [list](../../data-types/list).
[new_type](#new_type) | `collection` | A new [type](../../data-types/type) is added to the collection.
[set_type](#set_type) | `collection` | A [type](../../data-types/type) is initialized.
[del_type](#del_type) | `collection` | A [type](../../data-types/type) is removed from the collection.
[mod_type_add](#mod_type_add) | `collection` | A new field is added to an existing [type](../../data-types/type).
[mod_type_del](#mod_type_del) | `collection` | A field is removed from an existing [type](../../data-types/type).
[mod_type_mod](#mod_type_mod) | `collection` | A filed is modified on an existing [type](../../data-types/type).
[new_procedure](#new_procedure) | `collection` | A new procedure is added to the collection.
[del_procedure](#del_procedure) | `collection` | A procedure is removed from the collection.

{{% notice tip %}}
When *new* things are contained inside the mutations [set](#set), [add](#add) or [splice](#splice), Then the mutation will contain the *complete* thing with all properties. If on the other hand an *existing* thing is provided, then only the ID (`#`) and no other properties are contained.
{{% /notice %}}

## set

## del

## add

```thingsdb.syntax_only
// .myset = set();
.myset.add(#11, #23, {title: 'HG2G'});
```

> Adds the existing things `#11`, `#23` and a new thing `#42` to a *set* on property `myset`

```json
{
    "add": {
        "myset": [{
            "#": 11
        }, {
            "#": 23
        }, {
            "#": 42,
            "title": "HG2G"
        }]
    }
}
```

## remove

```thingsdb,syntax_only
// .myset = set(#55, #123, #42);
.myset.remove(#123, #42);
```

> Removes the things `#123` and `#42` are removed from a *set* on property `myset`

```json
{
    "remove": {
        "myset": [
            123,
            42
        ]
    }
}
```

## splice

```thingsdb,syntax_only
// .arr = ["a", "b"];
.arr.push("c", "d");
```

> Add items `"c"` and `"d"` at position `2`, and deletes `0` items to a *list* on property `arr`

```json
{
    "splice": {
        "arr": [2 , 0, "c", "d"]
    }
}
```

## new_type

## set_type

## del_type

## mod_type_add

## mod_type_del

## mod_type_mod

## new_procedure

```thingsdb,should_pass
new_procedure('multiply', |a, b| a*b);
```

> A new procedure named `multiply` is added to the collection

```json
{
    "new_procedure": {
        "name": "multiply",
        "created_at": 1579601906,
        "closure": "|a,b|a*b"
    }
}
```

## del_procedure
