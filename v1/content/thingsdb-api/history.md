---
title: "history"
weight: 363
---

List commit records from history based on a given filter.

### Function

`history(options)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`options`| thing | Options for filtering the commits to remove.

### Options

Option      | Type      | Description
----------- | --------- | -----------
`scope`     | str       | Can be either the `@thingsdb` or a `@collection` [scope](../../overview/scopes). This option is required ***only*** if [commit history](../set_history) is enabled on ***multiple*** scopes.
`detail`    | bool      | When `true`, the associated **code** for each commit will be included in the result (defaults to `false`).
`id`        | int       | Use the `id` option to retrieve a specific commit. When used, it overrides the standard list return, causing the function to return either the single matching commit or `nil` if that specific ID (combined with any other active filters) is not found.
`contains`  | str       | Filter commits where the given string is found in either **user name**, **message** or or associated **code**.
`match`     | regex     | Accepts a [regular expression](../../data-types/regex) used to selectively filter commits. A commit is included in the result set if the regular expression successfully matches any part of its **user name**, **message**, or associated **code**.
`first`     | int       | Takes an integer _"X"_ and limits the operation to the _"X"_ oldest records.
`last`      | int       | Takes an integer _"X"_ and limits the operation to the _"X"_ newest records.
`before`    | datetime  | Takes a [datetime](../../data-types/datetime) object to set an upper time limit. Only commits made before this exact date and time will be included.
`after`     | datetime  | Takes a [datetime](../../data-types/datetime) object to set an lower time limit. Only commits made after this exact date and time will be included.
`has_err`   | bool      | Setting it to `true` includes only commits where the query failed with an error, setting it to `false` includes only those that succeeded without error, and omitting the option or setting it to `nil` includes all commits regardless of success or failure.

This function does *not* generate a [change](../../overview/changes).

### Return value

List with commits as [mpdata](../../data-types/mpdata). However, if the `id` option is used, the return type changes to a single value: either the matching commit object or `nil` if no commit with that ID is found within the specified filters.

### Example

> This code lists all commits that contain the **exact word** "MyType" in the user, message, or code fields:

```thingsdb,syntax_only,@t
history({
    scope: '//stuff',
    detail: true,
    match: /\bMyType\b/
});
```

> Return value in JSON format

```json
[
    {
        "id": 345,
        "by": "admin",
        "created_on": "2025-11-06T10:35:12Z",
        "message": "Adds type MyType",
        "code": "commit('Adds type MyType'); new_type('MyType');"
    },
    {
        "id": 346,
        "by": "admin",
        "created_on": "2025-11-06T10:37:27Z",
        "message": "Adds type MyType",
        "code": "commit('Adds type MyType'); new_type('MyType');",
        "err_msg": "type `MyType` already exists"
    }
]
```
