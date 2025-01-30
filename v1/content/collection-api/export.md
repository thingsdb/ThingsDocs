---
title: "export"
weight: 223
---

This function can be used to export the collection structure as a readable string with ThingsDB code.
The function is also capable of exporting the full collection. This full collection export is returned as bytes which
then can be imported in a new collection using the [import(..)](../import) function.

Which method to use can be controlled with setting `dump` to either `true` or `false` (see [options](#options)).

{{% notice note %}}
This method must be used in a query **without** a [change](../../overview/changes). This restriction exists so ThingsDB can pack all things as-if they have new Id's which would not be possible when there were actually new things created.
{{% /notice %}}

This function does *not* generate a [change](../../overview/changes).

### Function

`export([options])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`options` | thing (optional) | A thing with optional [options](#options).

#### Options

Option | Type | Description
------ | ---- | -----------
`dump` | bool | When `true`, the export contains the full collection as [bytes](../../data-types/bytes) which can be used with the [import(..)](../import) function. The default is `false` which will export *only* the structure of the collection containing the enumerators, types and procedures in a readable [string](../../data-types/str).

### Return value

The name of the newly created Type.

### Example

> Export collection structure

```thingsdb,should_pass
export();  // output is a readable string with ThingsDB code
```

> Export the complete collection with all data

```thingsdb,should_pass
export({dump: true});  // output are bytes (see import function)
```
