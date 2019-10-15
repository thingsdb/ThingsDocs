+++
title = "Collection API"
date = 2019-10-07T11:04:33+02:00
weight = 13
chapter = true
+++

# Collection API

The *collection* scope can be used to manage data within a *collection*.

> This code returns the *id* of collection *stuff*

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q 'id()'
```

{{% notice tip %}}
The functions in the Collection API can also be used in the [thingsdb](../thingsdb-api) and [node](../node-api) scopes.
{{% /notice %}}
