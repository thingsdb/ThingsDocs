---
title: "Shell"
weight: 300
---

> Copy/paste to download and install *thingscmd*

```
pip install thingscmd
```

For running ThingsDB queries from the shell, a shell tool [ThingsCMD](https://github.com/thingsdb/ThingsCMD) is available.
It is not possible to *watch* things by using this shell based tool.

> To authorize from the shell, use this code:

```shell
# Authenticate with a user and password
thingscmd -n localhost -u admin -p pass -q "nil;"
# ..or with a token
thingscmd -n localhost -t "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" -q "nil;"

```
