---
title: "mpdata"
weight: 110
---


This is a special type within ThingsDB and is returned by all the `*_info()` functions.

As an example we can take the [node_info](../../node-api/node_info) and view the type. This will tell us that the value is indeed of the `mpdata` type.

```thingsdb,json_response,@n
// get the current node info
node_info = node_info();

// return the type as string to verify this is indeed the `info` type
type(node_info);
```

> Return value in JSON format

```json
"mpdata"
```

The `mpdata` type is also returned by default from all modules. This way ThingsDB does not require to load responses into memory if nothing has to be done with the result.

### Functions

Function | Description
------ | -----------
[len](./len) | Return the length of the data in bytes.
[load](./load) | Load the data into ThingsDB.
