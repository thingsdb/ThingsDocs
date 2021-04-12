---
title: "split"
weight: 106
---

Return a new [string](..) in which all case-based characters are in lower case.

This function does *not* generate an [event](../../../overview/events).

### Function

*str*.`split([separator], [limit])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
separator | str (optional) | The string used to split the original string. If omitted, white-space will be used as separator.
limit | int (optional) | Split at most `limit` times. If this value is negative, splitting starts from the end of the string. If omitted, no *limit* is used.

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
