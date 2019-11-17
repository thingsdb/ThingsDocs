---
title: "Query"
weight: 103
chapter: true
---

# Query

Queries to ThingsDB can be used to manage [nodes](../node-api), [ThingsDB](../thingsdb-api) or to query [collections](../collection-api).

A query request has a required field *scope* and *query*, and an option required field *collection* when querying a collection scope.

To send a query you can either use a language binding, see code examples, or if you
want to know how to serialize and send the data, read the [protocol](../protocol) section.

> Example query

```shell
thingscmd \
    --node        localhost \
    --user        admin      \
    --password    pass       \
    --scope       @thingsdb  \
    --query       "'Hello world!!'"
```

> Request in JSON format

```json
["@thingsdb", "'Hello world!!'"]
```
