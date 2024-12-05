---
title: "Start up node"
weight: 7
chapter: false
---

{{% notice note %}}
ThingsDB can _work_ with a single node but is designed to work with at least two nodes but three nodes are preferred.
Running on three nodes brings redundancy and ensures the database stays operational, even while you for example upgrade ThingsDB to a newer version.
{{% /notice %}}

After building the source code and making a symlink, you can start your first node using the following command. You need to add the `--init` flag to initialize a new ThingsDB store.

```bash
thingsdb --init
```

Starting a second (or other) node needs a secret.

```bash
thingsdb --secret second
```

The secret is used when adding this node; see [new_node](../../thingsdb-api/new_node) documentation on how to add a second (or other) node to ThingsDB.

## Flag information

| Flag                    | Description                                                                                                                                                                                                          |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-h`, `--help`          | Show the help message and exit.                                                                                                                                                                                      |
| `-c`, `--config CONFIG` | Define which ThingsDB [configuration file](https://github.com/thingsdb/ThingsDB/blob/main/thingsdb.example.conf) to use.                                                                                           |
| `--deploy`              | Auto set `--init` or `--secret` based on the `THINGSDB_NODE_NAME` and `THINGSDB_NODE_SECRET` [environment variable](../configuration). A use case is explained in the [next paragraph](#containerized-environments). |
| `--init`                | Initialize a new ThingsDB store.                                                                                                                                                                                     |
| `--force`               | Force `--init` or `--secret` to remove existing data if exists.                                                                                                                                                      |
| `--secret SECRET`       | Set one time secret and wait for request to join.                                                                                                                                                                    |
| `--rebuild`             | Rebuild the node (can only be used when having >1 nodes). A use case is explained in the [next paragraph](#fix-a-corrupted-node).                                                                                    |
| `--forget-nodes`        | Forget all nodes info and load ThingsDB with a single node. A use case is explained in the [next paragraph](#restore-from-backup).                                                                                   |
| `-v`, `--version`       | Show version information and exit.                                                                                                                                                                                   |
| `-l`, `--log-level`     | Set initial log level: _debug_, _info_, _warning_, _error_, _critical_.                                                                                                                                              |
| `--log-colorized`       | Use colorized logging.                                                                                                                                                                                               |
| `-y`, `--yes`           | Confirm questions with yes.                                                                                                                                                                                          |

### Flags as environment variable
Arguments are not supported in all cases. If needed, `--init`, `--secret` and `--deploy` can be replaced with enviroment variable.

Argument   | Environment variable | Description
---------- | -------------------- | -----------
`--init`   | `THINGSDB_INIT`      | Set to `1` to use `--init`, example: `THINGSDB_INIT=1`.
`--secret` | `THINGSDB_SECRET`    | Set some secret, example: `THINGSDB_SECRET=pass`.
`--deploy` | `THINGSDB_DEPLOY`    | Set to `1` to use `--deploy`, example: `THINGSDB_DEPLOY=1`.


## Use cases

### Containerized environments

In containerized environments like kubernetes it is often useful to initialize automatically based on the node name.
The `--deploy` argument is created for this purpose and triggers the following behavior.

- If the node name ends with `-0`, the node is considered to be the first node and will automatically set
  the `--init` argument in case the node is started for the first time.
- If the node does not end with `-0`, then the node will be started with `--secret` when the node is started
  for the first time. The secret will be equal to the node name unless the environment
  variable `THINGSDB_NODE_SECRET` is set.

### Restore from backup

When you need to restore from a back up you will need to set the environment variable `THINGSDB_STORAGE_PATH` to the latest backup file (.tar.gz). Then you can start ThingsDB again with the following command:

```bash
thingsdb --forget-nodes
```

The `--forget-nodes` flag is in this case very useful. The flag causes to forget all nodes. You can just start with one node without getting in a situation where the [quorum](../../overview/dictionary) will not be reached when multiple nodes are down. After the first node has started you can then simply add other nodes again.

### Fix a corrupted node

When you get in the situation that one of your nodes is corrupted for some reason, you can shutdown the node and start it again with the following flag:

```bash
thingsdb --rebuild
```

This causes the node to wipe its corrupted data and synchronize again with one of the other healthy nodes.

Using the `--rebuild` flag is a simplified way of doing the following but same thing. You shutdown the corrupted node. Delete it as well, so the other nodes forget about this node. Then start the node again with the following command:

```bash
thingsdb --force
```

The `--force` flag causes to wipe all the stored data and start fresh. Then you can add this node again to the ThingsDB store.

As you will notice this takes a couple of more steps, so it is easier to just use the `--rebuild` flag.
