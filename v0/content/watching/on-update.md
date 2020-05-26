---
title: "on-update"
weight: 222
---

An update event is pushed when changes are made to a `thing` you are watching.
Nested things need to be watched separately.

The event contains the Thing ID (`#`), an event number, and a *jobs* array containing all the mutations to the thing in the  applied order.

```json
{
    "#": 3,
    "event": 123,
    "jobs": [
        ...mutations
    ]
}
```

Each mutation is a *map* `{}` with a single *key*. This key tells what kind of *mutation* is applied to the thing. If the *thing* is actually a collection, you will receive both
changes to the *thing*, as well as changes to the *collection*. This way you can also watch for collection mutations such as Type or procedure changes.

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
[mod_type_mod](#mod_type_mod) | `collection` | A field is modified on an existing [type](../../data-types/type).
[mod_type_del](#mod_type_del) | `collection` | A field is removed from an existing [type](../../data-types/type).
[new_procedure](#new_procedure) | `collection` | A new procedure is added to the collection.
[del_procedure](#del_procedure) | `collection` | A procedure is removed from the collection.

{{% notice tip %}}
When *new* things are added via the mutations [set](#set), [add](#add) or [splice](#splice), Then the mutation will contain the *complete* thing with all properties. If on the other hand an *existing* thing is provided, then only the ID (`#`) is included.
{{% /notice %}}

{{% notice info %}}
While most values inside mutation are easy to understand, a instance of a *Type* might seem a bit strange. For help with parsing such mutations see the [set](#set) example below, and the [mutation format](../../data-types/type#mutation-format) documentation.
{{% /notice %}}

## set

```thingsdb,syntax_only
// Adds a property `name` with value `"ThingsDB"`.

.name = "ThingsDB";
```

> Mutation result from the above code:

```json
{
    "set": {
        "name": "ThingsDB"
    }
}
```

Most values like the one above are quite obvious but note that instances of
a certain [Type](../../data-types/type) use the `type_id` and refer to fields
with the values instead of the property names. For example:

```thingsdb,syntax_only
// set_type('Person', {name: 'str'});

.person = Person{name: "Iris"};
```

The mutation event of creating the `Person` above contains an empty key `""` with
an `array` of *fields*. They refer to the *fields* of the Type with `type_id:0`
which can be found at key `"."`. The ID of the instance is equal to a normal *thing*
and can be found with key `"#"`, so the ID is 5 in the example result below. For more
information on how to parse a Type instance, look at the [mutation format](../../data-types/type#mutation-format) documentation.

```json
{
    "set": {
        "person": {
            "": [
                "Iris"
            ],
            "#": 5,
            ".": 0
        }
    }
}
```

## del

```thingsdb,syntax_only
// Delete property `name`.

// .name = "ThingsDB";
.del("name");
```

> Mutation result from the above code:

```json
{
    "del": "name"
}
```

## add

```thingsdb,syntax_only
/*
 * Adds the existing things `#11`, `#23` and a new
 * thing `#42` to a *set* on property `myset`.
 */

// .myset = set();
.myset.add(#11, #23, {title: 'HG2G'});
```

> Mutation result from the above code:

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
/*
 * Removes the things `#123` and `#42` are removed
 * from a *set* on property `myset`.
 */

// .myset = set(#55, #123, #42);
.myset.remove(#123, #42);
```

> Mutation result from the above code:

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
/*
 * Add items `"c"` and `"d"` at position `2`, and
 * deletes `0` items to a *list* on property `arr`.
 */

// .arr = ["a", "b"];
.arr.push("c", "d");
```

> Mutation result from the above code:

```json
{
    "splice": {
        "arr": [2 , 0, "c", "d"]
    }
}
```

## new_type

```thingsdb,should_pass
/*
 * A new Type named `Person` is added to the collection
 * The `type_id` is usually not something you use, except
 * for other mutations which refer to `type_id` when creating
 * an instance of a Type.
 */

new_type('Person');
```

> Mutation result from the above code:

```json
{
    "new_type": {
        "created_at": 1581453937,
        "name": "Person",
        "type_id": 0
    }
}
```

## set_type

```thingsdb,should_pass
/*
 * Set initial Type field definitions, field `name`
 * with definition `str` on type `Person` in this case.
 */

set_type('Person', {name: 'str'});
```

> Mutation result from the above code:

```json
{
    "set_type": {
        "fields": [
            ["name", "str"]
        ],
        "modified_at": 1581455876,
        "type_id": 0
    }
}
```

## del_type

```thingsdb,syntax_only
// Delete a Type named `Person`.

// new_type('Person');
del_type('Person');
```

> Mutation result from the above code:

```json
{
    "del_type": 0
}
```

## mod_type_add

```thingsdb,syntax_only
/*
 * Add a new field `rating` to type `Book`. If, and only if existing instances
 * of the type `Book` exist, the mutation contains an `init` field with
 * the given initial value. This value can be used to update earlier loaded
 * instances of type `Book` and may be updated with this initial value to stay
 * consistent with ThingsDB.
 */

// set_type('Book', {title: 'str'}); .book = Book{title: 'hhgttg'};
mod_type('Book', 'add', 'rating', 'uint', 1);
```

> Mutation result from the above code:

```json
{
    "mod_type_add": {
        "init": 1,
        "modified_at": 1581510638,
        "name": "rating",
        "spec": "uint",
        "type_id": 2
    }
}
```

## mod_type_mod

```thingsdb,syntax_only
// Change field definition `rating` of type `Book`.

// set_type('Book', {title: 'str', rating: 'uint'});
mod_type('Book', 'mod', 'rating', 'number');
```

> Mutation result from the above code:

```json
{
    "mod_type_mod": {
        "modified_at": 1581511115,
        "name": "rating",
        "spec": "number",
        "type_id": 2
    }
}
```

## mod_type_del

```thingsdb,syntax_only
// Delete the `rating` field definition of type `Book`.

// set_type('Book', {title: 'str', rating: 'number'});
mod_type('Book', 'del', 'rating');
```

> Mutation result from the above code:

```json
{
    "mod_type_del": {
        "modified_at": 1581511233,
        "name": "rating",
        "type_id": 2
    }
}
```

## new_procedure

```thingsdb,should_pass
// A new procedure named `multiply` is added to the collection.

new_procedure('multiply', |a, b| a*b);
```

> Mutation result from the above code:

```json
{
    "new_procedure": {
        "name": "multiply",
        "created_at": 1579601906,
        "closure": {
            "/": "|a,b|a*b"
        }
    }
}
```

## del_procedure

```thingsdb,syntax_only
// Delete a  procedure named `multiply`.

// new_procedure('multiply', |a, b| a*b);
del_procedure('multiply');
```

> Mutation result from the above code:

```json
{
    "del_procedure": "multiply"
}
```
