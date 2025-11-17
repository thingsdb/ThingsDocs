---
title: "del_history"
weight: 352
---

Delete commit records from history based on a given filter.

### Function

`del_history(options)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`options`| thing | Options for filtering the commits to remove.

### Options

Option      | Type      | Description
----------- | --------- | -----------
`scope`     | str       | Can be either the `@thingsdb` or a `@collection` [scope](../../overview/scopes). This option is required ***only*** if [commit history](../set_history) is enabled on ***multiple*** scopes.
`id`        | int       | Use `id` to delete a specific commit.
`contains`  | str       | Filter commits where the given string is found in either **user name**, **message** or or associated **code**.
`match`     | regex     | Accepts a [regular expression](../../data-types/regex) used to selectively filter commits. A commit is included in the result set if the regular expression successfully matches any part of its **user name**, **message**, or associated **code**.
`first`     | int       | Takes an integer _"X"_ and limits the operation to the _"X"_ oldest records. ***only
`last`      | int       | Takes an integer _"X"_ and limits the operation to the _"X"_ newest records.
`before`    | datetime  | Takes a [datetime](../../data-types/datetime) object to set an upper time limit. Only commits made before this exact date and time will be included.
`after`     | datetime  | Takes a [datetime](../../data-types/datetime) object to set an lower time limit. Only commits made after this exact date and time will be included.
`has_err`   | bool      | Setting it to `true` includes only commits where the query failed with an error, setting it to `false` includes only those that succeeded without error, and omitting the option or setting it to `nil` includes all commits regardless of success or failure.

Use the [history()](../../thingsdb-api/history) function to view the commits in the history log.

This function generates a [change](../../overview/changes).

### Return value

Returns the number of removed `commits`.

### Example

> This code **Deletes** all commits that were created **more than six months ago** in the `//stuff` collection:

```thingsdb,syntax_only,@t
del_history({
    scope: '//stuff',
    before: datetime().move('months', -6),
});
```

> Return value in JSON format

```json
42
```
