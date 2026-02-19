---
title: "type_all"
weight: 328
---

Returns a [set](../../data-types/set) with all instances of a given [Type](../../overview/type) within a collection.

{{% notice tip %}}
To optimize performance for frequent `type_all(..)` requests, enable [auto-index](../../collection-api/mod_type/idx). This caches type metadata, resulting in significantly faster response times.
{{% /notice %}}

This function does *not* generate a [change](../../overview/changes).

### Function

`type_all(type)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | The name of the Type for which the instances must be returned.

### Return value

A [set](../../data-types/set) with all occurrences of the given [Type](../../overview/type) within a collection.
