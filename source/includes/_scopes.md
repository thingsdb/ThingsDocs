# Scopes
When sending a query, calling a procedure or subscribing to a thing, the request
will require you to provide a scope. ThingsDB has three main scopes: *@thingsdb*, *@node* and *@collection*.


scope | short | description
----- | ----- | -----------
`@thingsdb` | `@t` | ThingsDB scope; Used for managing user accounts, collections and nodes.
`@node` | `@n` | Current node scope; For node info and statistics from the connected node.
`@node:ID` | `@n:ID` | Specific node scope; Get node info and statistics from a specific node id (`ID` should be replaced with a node ID, for example `0`).
`@collection:NAME` | `@:NAME` | Collection scope; A collection where things are stored.
`@collection:ID` | `@:ID` | Collection scope; By collection `ID` instead of the using the collection name.
