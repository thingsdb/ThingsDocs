---
title: "split"
weight: 143
---

Return a new [string](..) in which all case-based characters are in lower case.

This function does *not* generate a [change](../../../overview/changes).

### Function

*str*.`split([separator], [limit])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
separator | str/regex (optional) | The string used to split the original string. If omitted, white-space will be used as separator. Instead of a string, a regular expression may be used as well, see [regular expression](#regular-expression).
limit | int (optional) | Split at most `limit` times. If this value is negative, splitting starts from the end of the string. If omitted, no *limit* is used.

### Regular expression

If separator is a [regular expression](../../regex) with capturing parentheses, then each time separator matches, the results of the capturing parentheses are added into the output list.

### Return value

Returns a new list with substrings.

### Examples

> Example using ***split()*** without arguments:

```thingsdb,json_response
'How are you doing?'.split();
```

> Return value in JSON format

```json
[
    "How",
    "are",
    "you",
    "doing?"
]
```

> Example using ***split()*** with a *limit*:

```thingsdb,json_response
'This is a test'.split(1);
```

> Return value in JSON format

```json
[
    "This",
    "is a test"
]
```

> Example using ***split()*** with a negative *limit*:

```thingsdb,json_response
'This is a test'.split(-1);
```

> Return value in JSON format

```json
[
    "This is a",
    "test"
]
```


> Example using ***split()*** with a *separator*:

```thingsdb,json_response
'title,subject,body'.split(',');
```

> Return value in JSON format

```json
[
    "title",
    "subject",
    "body"
]
```

> Example using ***split()*** with a *regular expression*:

```thingsdb,json_response
'Found 143 songs of 3 minutes and 45 seconds.'.split(/\d+/);
```

> Return value in JSON format

```json
[
    "Found ",
    " songs of ",
    " minutes and ",
    " seconds."
]
```

> Example using ***split()*** with a *regular expression* and *capture groups*:

```thingsdb,json_response
'Found 143 songs of 3 minutes and 45 seconds.'.split(/\s*(\d+)\s*/);
```

> Return value in JSON format

```json
[
    "Found",
    "143",
    "songs of",
    "3",
    "minutes and",
    "45",
    "seconds."
]
```
