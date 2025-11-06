---
title: "commit"
weight: 215
---

Saves a commit for the current query.

This function requires that the query makes a [change](../../overview/changes), _and_ that [commit history](../../thingsdb-api/set_history) has been enabled for the relevant scope.

{{% notice note %}}
Use **commit(..)*** only for collection structural changes like set-up or migration scripts.
It is _not_ intended for routine "normal" operations that your application performs during its regular runtime.
{{% /notice %}}

Use the [history()](../../thingsdb-api/history) function to view the commits in the history log.

This function does *not* generate a [change](../../overview/changes).

### Function

`commit(message)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message  | str  | The commit message.

### Return value

The value `nil`.

### Example

> This code creates a commit:

```thingsdb,syntax_only
commit('Adds type "T"');

new_type('T');
```

> Return value in JSON format

```json
"T"
```
