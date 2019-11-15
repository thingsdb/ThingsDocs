---
title: "Arguments"
date: 2019-10-14T09:31:27+02:00
---

Arguments can be used when querying ThingsDB.

Can also be used for binary data, see example.

> This code uses arguments to set binary data using *arguments*:

```shell
# note: ThingsCMD only supports one argument which is named `blob`
curl "https://docs.thingsdb.net/images/logo.png" |
thingscmd -n node.local -u admin -p pass -c @:stuff -q  ".logo = blob;"
```