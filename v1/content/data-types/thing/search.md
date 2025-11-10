---
title: "search"
weight: 185
---

Find the parent(s) of a given thing.

{{% notice warning %}}
This function is useful for **debugging purposes** and must **not be used in production** queries as the function isn't optimized for speed.
{{% /notice %}}

This function does *not* generate a [change](../../../overview/changes).

### Function

*thing*.`search(needle, [options])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
needle | thing | The _thing_ to search.
options | thing | Thing with [options](#options).

### Options

Option | Type | Description
------ | ---- | -----------
deep   | int  | Specify how [deep](../../../collection-api/deep) the thing must be searched. (defaults to 1)
limit  | int  | Specify a limit of how many results must be search for. (defaults to 1)

### Return value

Returns a new list with search results. An empty list is returned if nothing is found.
Each result contains a thing with a `parent`, `parent_type`, `key` and `key_type`.

### Example

> Using `search()` to find a thing with id 123 using deep level 5:

```thingsdb,syntax_only
.search(thing(123), {deep: 5});
```

> Return value in JSON format

```json
[
    {
        "key": "example",
        "key_type": "thing",
        "parent": {
            "#": 3
        },
        "parent_type": "thing"
    }
]
```

> The above result means that thing with Id 123 can be found at `thing(3).example`
