---
title: "Dictionary"
weight: 28
---

The following list contains definitions specific for ThingsDB:

Keyword | Definition
------ | :----------
Collection |The [collection](../collections) is the root thing. Every collection has its own scope.
Computed properties |With [computed properties](../../data-types/wtype#computed-properties) it is possible to return computed values by wrapping a [Type](../../data-types/type).
Closure |A [Closure](../../data-types/closure) is a user defined method which can be saved. It can be used as a prepared piece of code or to consume items from a `thing`, `list`, `tuple` or `set`.
Change |ThingsDB creates a [change](../changes) when a query modifies something.  Changes are applied in order by each node to guarantee consistency.
Function |Function in ThingsDB means a built in function. A function needs the exact number of arguments that is expected, which is different for a closure or procedure.
Node |[Node](../../node-api) is the process running ThingsDB. ThingsDB can *work* with a single node but is designed to work with multiple nodes. Running on at least three nodes brings redundancy and ensures the database stays operational.
Procedure |A [procedure](../../procedures-api) in ThingsDB is a named closure that is attached to a scope (*@thingsdb* or *@collection*) and available to use in an API call.
Relation | Relations can be created between [Types](../../data-types/type) or even within a single [Type](../../data-types/type) and can be used to create a two-way relation between instances. See [mod_type, action: rel](../../collection-api/mod_type/rel/).
Scope |When sending a query, calling a procedure or subscribing to a thing, the request will require you to provide a scope. ThingsDB has three [scope](../scopes) categories: *@thingsdb*, *@node* and *@collection*.
Thing |A thing is an object to which properties can be assigned.
Quorum | ThingsDB ensures consistency across multiple nodes. This is achieved by *changes*. Changes get an Id which are in applied order. Before a node can assign an Id to a *change*, it needs approval of the majority of the existing nodes. Once a node has connected to the others, it takes part in the quorum. If a node goes down it still gets accounted for, but will negatively influence the quorum as it cannot respond. When a node is deleted it does not take part in the quorum anymore.
Zone | When a node is in "away" mode, queries to a collection or ThingsDB scope will be forwarded to another node. If zones are configured, the node will first try a node within the same zone; only if no other node in the same zone is available, another node in another zone will be used.
