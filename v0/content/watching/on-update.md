---
title: "on-update"
weight: 299
---

An update event is pushed when changes are made to a `thing` you are watching.
Nested things need to be watched separately.

The event contains the Thing Id (`#`), an event number, and a *jobs* array containing all the mutations to the thing in the  applied order.

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
[event](#event) | `thing` | An event is emitted.
[new_type](#new_type) | `collection` | A new [type](../../data-types/type) is added to the collection.
[set_type](#set_type) | `collection` | A [type](../../data-types/type) is initialized.
[del_type](#del_type) | `collection` | A [type](../../data-types/type) is removed from the collection.
[mod_type_add](#mod_type_add) | `collection` | A new field is added to an existing [type](../../data-types/type).
[mod_type_del](#mod_type_del) | `collection` | A field is removed from an existing [type](../../data-types/type).
[mod_type_mod](#mod_type_mod) | `collection` | A field is modified on an existing [type](../../data-types/type).
[mod_type_ren](#mod_type_ren) | `collection` | A field is renamed on an existing [type](../../data-types/type).
[mod_type_wpo](#mod_type_wpo) | `collection` | Wrap-only mode is changed for a [type](../../data-types/type).
[set_enum](#set_enum) | `collection` | A new [enum](../../data-types/enum) type is created.
[del_enum](#del_enum) | `collection` | An [enum](../../data-types/enum) type is removed from the collection.
[mod_enum_add](#mod_enum_add) | `collection` | A new member is added to an existing [enum](../../data-types/enum).
[mod_enum_def](#mod_enum_def) | `collection` | The default member is changed for an existing [enum](../../data-types/enum).
[mod_enum_del](#mod_enum_del) | `collection` | A member is removed from an existing [enum](../../data-types/enum).
[mod_enum_mod](#mod_enum_mod) | `collection` | A member value is modified on an existing [enum](../../data-types/enum).
[mod_enum_ren](#mod_enum_ren) | `collection` | A member name is modified on an existing [enum](../../data-types/enum).
[new_procedure](#new_procedure) | `collection` | A new procedure is added to the collection.
[del_procedure](#del_procedure) | `collection` | A procedure is removed from the collection.

{{% notice tip %}}
When *new* things are added via the mutations [set](#set), [add](#add) or [splice](#splice), Then the mutation will contain the *complete* thing with all properties. If on the other hand an *existing* thing is provided, then only the Id (`#`) is included.
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
which can be found at key `"."`. The Id of the instance is equal to a normal *thing*
and can be found with key `"#"`, so the Id is 5 in the example result below. For more
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

Mutations on a list are always converted to a `splice` event. From this it follows that
no matter when using [splice](../../data-types/list/splice), [push](../../data-types/list/push),
[pop](../../data-types/list/pop) or another function to make modifications to a list,
the resulting event contains a `splice` mutation.

```thingsdb,syntax_only
/*
 * Add items `"c"` and `"d"` at position `2`, and
 * deletes `0` items to a *list* on property `arr`.
 */

// .arr = ["a", "b"];
.arr.push("c", "d");
```

> Mutation result from the above code: *(at position 2, 0 deletions, and 2 new items)*

```json
{
    "splice": {
        "arr": [2 , 0, "c", "d"]
    }
}
```


## event

Events are always triggered using the [emit(..)](../../data-types/thing/emit) function.

```thingsdb,should_pass
.emit("greet", "Hello", "universe!");
```

> Mutation result from the above code:

```json
{
    "event": [
        "greet",
        "Hello",
        "universe!"
    ]
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
        "type_id": 0,
        "wrap_only": false
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
        "methods": {},
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

Instead of adding a new field using a default value, it is possible to use a closure to generate
initial values *(see [mod_type(..add)](../../collection-api/mod_type/add))*. In this case the following mutations are pushed
to watchers:

1. Mutation `mod_type_add`.
2. Things with initial value *other than* the default value will receive a `set` mutation with the new initial value.


## mod_type_del

{{% notice note %}}
Delete is always performed using a `swap_remove` *(the removed value will be replaced with the last value)*. For example when having the type properties `[A, B, C, D]` and then remove `B` will result in  `[A, D, C]`.
{{% /notice %}}


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

Instead of migrating to a `less` strict definition, it is possible to use a closure
and migrate to a complete new definition *(see [mod_type(..mod)](../../collection-api/mod_type/mod))*. In this case the following mutations are pushed
to watchers:

1. Mutation `mod_type_mod` with a `any` spec.
2. At *least* things with incompatible data on the field will receive a `set` mutation with a new value according the new spec.
3. Mutation `mod_type_mod` with the required spec.


## mod_type_ren

```thingsdb,syntax_only
// Rename the `rate` field of type `Book` to `rating`.

// set_type('Book', {title: 'str', rate: 'number'});
mod_type('Book', 'ren', 'rate', 'rating');
```

> Mutation result from the above code:

```json
{
    "mod_type_ren": {
        "modified_at": 1581511233,
        "name": "rate",
        "to": "rating",
        "type_id": 2
    }
}
```

## mod_type_wpo

```thingsdb,syntax_only
// Enable wrap-only mode

// set_type('Book', {title: 'str', rate: 'number'});
mod_type('Book', 'wpo', true);
```

> Mutation result from the above code:

```json
{
    "mod_type_wpo": {
        "modified_at": 1581511233,
        "wrap_only": true,
        "type_id": 2
    }
}
```

## set_enum

```thingsdb,should_pass
/*
 * Create and set initial enumerator.
 */

set_enum('Color', {
    RED: '#f00',
    GREEN: '#0f0',
    BLUE: '#00f'
});
```

> Mutation result from the above code:

```json
{
    "set_enum": {
        "created_at": 1581455876,
        "enum_id": 0,
        "name": "Color",
        "members": [
            ["RED", "#f00"],
            ["GREEN", "#0f0"],
            ["BLUE", "#00f"]
        ]
    }
}
```

## del_enum

```thingsdb,syntax_only
// Delete a enumerator named `Color`.

del_enum('Color');
```

> Mutation result from the above code:

```json
{
    "del_enum": 0
}
```

## mod_enum_add

```thingsdb,syntax_only
// Add a member `BLUE` to enumerator `Color`.

// set_enum('Color', {RED: '#f00', GREEN: '#0f0'});
mod_enum('Color', 'add', 'BLUE', '#00f');
```

> Mutation result from the above code:

```json
{
    "mod_type_add": {
        "enum_id": 2,
        "modified_at": 1581511233,
        "name": "BLUE",
        "value": "#00f"
    }
}
```

## mod_enum_def

{{% notice note %}}
Defaults are always changed using a `swap` with the previous default. For example when having the enum values `[A, B, C, D]` and then change the default from `A` to `C` will result in order `[C, B, A, D]`.
{{% /notice %}}

```thingsdb,syntax_only
// Set member `GREEN` as the default member for enumerator `Color`.

// set_enum('Color', {RED: '#f00', GREEN: '#0f0', BLUE: '#00f'});
mod_enum('Color', 'def', 'GREEN');
```

> Mutation result from the above code:

```json
{
    "mod_enum_def": {
        "enum_id": 2,
        "index": 1,
        "modified_at": 1581511233
    }
}
```

## mod_enum_del

{{% notice note %}}
Delete is always performed using a `swap_remove` *(the removed value will be replaced with the last value)*. For example when having the enum members `[A, B, C, D]` and then remove `B` will result in  `[A, D, C]`.
{{% /notice %}}


```thingsdb,syntax_only
// Delete member `GREEN` from enumerator `Color`.

// set_enum('Color', {RED: '#f00', GREEN: '#0f0', BLUE: '#00f'});
mod_enum('Color', 'del', 'GREEN');
```

> Mutation result from the above code:

```json
{
    "mod_enum_del": {
        "enum_id": 2,
        "index": 1,
        "modified_at": 1581511233
    }
}
```

## mod_enum_mod

```thingsdb,syntax_only
// Modify the value of member `BLUE` on enumerator `Color`.

// set_enum('Color', {RED: '#f00', GREEN: '#0f0', BLUE: '#fff'});
mod_enum('Color', 'mod', 'BLUE', '#00f');
```

> Mutation result from the above code:

```json
{
    "mod_enum_mod": {
        "enum_id": 2,
        "index": 2,
        "modified_at": 1581511233,
        "value": "#00f"
    }
}
```

## mod_enum_ren

```thingsdb,syntax_only
// Rename member `MOON` to `BLUE` of enumerator `Color`.

// set_enum('Color', {RED: '#f00', GREEN: '#0f0', MOON: '#00f'});
mod_enum('Color', 'ren', 'MOON', 'BLUE');
```

> Mutation result from the above code:

```json
{
    "mod_enum_ren": {
        "enum_id": 2,
        "index": 2,
        "modified_at": 1581511233,
        "name": "BLUE"
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
