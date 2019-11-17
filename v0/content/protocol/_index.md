---
title: "Protocol"
weight: 3
chapter: true
---

# Protocol

This is a more in depth view of the protocol used for communication with ThingsDB.
In case you just want to use ThingsDB using one of the language bindings, then this
info can be skipped. If you plan to implement you own connector, then this info might
be useful to you.

Communication with ThingsDB is done over a socket, either using TCP or a UNIX PIPE connection.
Once a connection is made, packages can be send to ThingsDB. Each package starts
with a 8 bytes header using little endian, followed by optional data. Before you can
send queries to ThingsDB, the connection must be authenticated. This can be done by
sending an `AUTH` package.
