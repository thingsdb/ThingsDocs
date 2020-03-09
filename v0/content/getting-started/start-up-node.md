---
title: "Start up node (Linux)"
weight: 4
chapter: false
---

{{% notice note %}}
ThingsDB can *work* with a single node but is designed to work with at least two nodes but three nodes are preferred.
Running on three nodes brings redundancy and ensures the database stays operational, even while you for example upgrade ThingsDB to a newer version.
{{% /notice %}}

After building the source code, making a symlink and a configuration file, you can start your first node using the following command. You need to add the `--init` flag to initialize a new ThingsDB store.

```
thingsdb -c ./thingsdb.example.conf --init
```

Starting a second (or other) node needs a secret that identifies it.

```
thingsdb -c ./thingsdb.example2.conf --secret second
```

The secret is used when adding a node; see [new_node](../../thingsdb-api/new_node) documentation on how to add this second (or other) node to ThingsDB.

## Flag information

Flag | Description
----- | ----- | -----------
`-h`, `--help` | Show the help message and exit.
`-c`, `--config CONFIG` | Define which ThingsDB configuration file to use.
`--deploy` | Auto set `--init` or `--secret` based on the `THINGSDB_NODE_NAME` and `THINGSDB_NODE_SECRET` environment variable. A use case is explained in the [next paragraph](#managed-containerized-environments).
`--init` | Initialize a new ThingsDB store.
`--force` | Force `--init` or `--secret` to remove existing data if exists.
`--secret SECRET` | Set one time secret and wait for request to join.
`--rebuild` | Rebuild the node (can only be used when having >1 nodes).
`--forget-nodes` | Forget all nodes info and load ThingsDB with a single node.
`-v`, `--version` | Show version information and exit.
`-l`, `--log-level` | Set initial log level: *debug*, *info*, *warning*, *error*, *critical*.
`--log-colorized` | Use colorized logging.

### Managed, containerized environments
In managed, containerized environments like kubernetes it is often useful to initialize automatically based on the node name.
The `--deploy` argument is created for this purpose and triggers the following behavior.

- If the node name ends with `-0`, the node is considered to be the first node and will automatically set
   the `--init` argument in case the node is started for the first time.
- If the node does not end with `-0`, then the node will be started with `--secret` when the node is started
   for the first time. The secret will be equal to the node name unless the environment
   variable `THINGSDB_NODE_SECRET` is set.
