---
title: "rel"
weight: 266
---

Add or delete a relation between properties of the same or different types.

Relations can only be created between *nillable* type definitions and/or restricted sets. This results in the following combinations:

Combination | Description
----------- | -----------
`Type?` <-> `Type?` | One to one relation.
`Type?` <-> `{Type}`| One to many relation.
`{Type}` <-> `{Type}` | Many to many relation.

All missing relations on existing instances will be automatically created by ThingsDB once you add a new relation. Relations only work on stored things.

{{% notice info %}}
With a ***one-to-one*** or a ***one-to-many*** relation it may not be possible to automatically create all missing relations because
you might be in a state where the existing instances are not related correctly. For example, you want to create a ***one-to-many*** relation but one of the *things*
exists in a *set* on another *thing* than being referenced to. Either the *set* or the *reference* is obviously incorrect. In such state ThingsDB will raise a [type_err()](../../../errors/type_err) and does not
create the relation.
{{% /notice %}}

### Action

`mod_type(type, 'rel', property, to)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | Name of the Type where to set the wrap-mode for.
`'rel'` | str | Passing this argument will result in a *relation* action.
property | str | Property to create a relation for.
to | str/nil | Property on the *other* type to create a relation with. When `nil`, an existing relation will be removed.

### Return value

The value `nil`.

### Example

> This code shows a one-to-many relation between two types:

```thingsdb,json_response
new_type('Workspace');
new_type('Person');

set_type('Workspace', {
    people: '{Person}'
});

set_type('Person', {
    workspace: 'Workspace?'
});

/* Create a relation between Person.workspace and Workspace.people
 *
 * Note: We could have used mod_type('Workspace', ...); just as well,
 *       it does not matter from which direction the relation is made.
 */
mod_type('Person', 'rel', 'workspace', 'people');

// Create a workspace
.foo = Workspace{};

// Create a person and assign workspace `foo`:
alice = Person{};
.foo.people.add(alice);

// THe workspace of Alice is automatically set to foo
alice.workspace == .foo;  // true
```

> Return value in JSON format

```json
true
```

Another example using a many-to-many relation within a single type:

```thingsdb,json_response
new_type('Album');

set_type('Album', {
    title: 'str',
    similar: '{Album}'
});

// Create a relation for Album.similar
mod_type('Album', 'rel', 'similar', 'similar');

.hoss = Album{title: 'Hoss'};
.punk_in_drublic = Album{title: 'Punk in Drublic'};

// Add `punk_in_drublic` as a similar album to `hoss`
.hoss.similar.add(.punk_in_drublic);

// note that `hoss` is also added as a similar album to `punk_in_drublic`:
.punk_in_drublic.similar.has(.hoss);  // true
```

> Return value in JSON format

```json
true
```
