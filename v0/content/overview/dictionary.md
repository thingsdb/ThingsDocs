---
title: "Dictionary"
weight: 22
---

The following list contains definitions specific for ThingsDB:



Keyword | Definition
------ | :----------
Qourum | ThingsDB ensures consistency acrrosss multiple nodes. This is achieved by events. Events get an ID which are in applied order. Before a node can assign an ID to an event, it needs approval of the majority of the existing nodes. Once a node has connected to the others, it takes part in the quorum. If a node goes down it still gets accounted for, but will negatively influence the quorum as it cannot repond. When a node is deleted it does not take part in the quorum anymore. 
Zone | When a node is in "away" mode, queries to a collection or ThingsDB scope will be forwarded to another node. If zones are configured, the node will first try a node within the same zone; only if no other node in the same zone is available, another node in another zone will be used. 
