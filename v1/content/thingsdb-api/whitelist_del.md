---
title: "whitelist_del"
weight: 378
---

Deletes an existing rule from a whitelist or removes all rules, effectively disabling the whitelist.

For more details, see [whitelist_add](../whitelist_add).

This function generates a [change](../../overview/changes).

### Function

`whitelist_del(user, whitelist, [rule])`

### Arguments

Argument    | Type                  | Description
----------- | --------------------- | -----------
`user`      | str (required)        | Username for which to delete the whitelist.
`whitelist` | str (required)        | The whitelist. Either `"procedures"` or `"rooms"`.
`rule`      | str/regex (optional)  | Either a name for the procedure/room or a regular expression to match potentially multiple procedures or rooms. If omitted, the whitelist will be removed.

### Return value

Returns `nil` if successful.

### Example

> Create a new user `iris` and apply a whitelist.

```thingsdb,syntax_only,@t
// Remove the "rooms" whitelist for user "iris".
whitelist_del('iris', 'rooms');
```

> Return value in JSON format

```json
null
```
