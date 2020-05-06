---
title: "info"
weight: 40
---


This is a special type within ThingsDB and is returned by all the `*_info()` functions.

As an example we can take the [node_info](../../node-api/node_info) and view the type. This will tell us that the value is indeed of the `info` type.

```thingsdb,json_response,@n
// get the current node info
node_info = node_info();

// return the type as string to verify this is indeed the `info` type
type(node_info);
```

> Return value in JSON format

```json
"info"
```
