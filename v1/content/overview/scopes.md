---
title: "Scopes"
weight: 24
---

When sending a query, calling a procedure or subscribing to a thing, the request
will require you to provide a scope. ThingsDB has three scope categories: *@thingsdb*, *@node* and *@collection*.

scope | short | description
----- | ----- | -----------
`@thingsdb` | `@t` | ThingsDB scope; Used for managing user accounts, collections and nodes.
`@node` | `@n` | Current node scope; For node info and statistics from the connected node.
`@node:ID` | `@n:ID` | Specific node scope; Get node info and statistics from a specific node Id (`Id` should be replaced with a node ID, for example `0`).
`@collection:NAME` | `@:NAME` | [Collection](../collections) scope; A collection where things are stored.

{{% notice tip %}}
Scopes names do allow an alternative syntax where the `@` and `:` are replaced with the `/` character.
For example `@collection:stuff` can be written as `/collection/stuff` and the short version `@:stuff` may be written as `//stuff`.
{{% /notice %}}
