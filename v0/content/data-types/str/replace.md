---
title: "replace"
weight: 108
---

Return a new [string](..) in which in which the occurrences of *old* have been replaced with *new*.
Optionally, the *number* of replacements can be restricted and may start from either left or right.

This function does *not* generate an [event](../../../overview/events).

### Function

*str*.`replace(old, new, [number])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
old | str (required) | The old substring to replace.
limit | str (required) | String which will replace the *old* substring.
number | int (optional) | Maximum number of replacements. If not given, all occurrences of the *old* substring will be replaced. If *negative*, replacement starts at the end of the string.


### Return value

Returns a new string with all occurrences of *old* have been replaced with *new*, optionally limited by a maximum *number* of replacements.

### Example

> Example using ***replace()***:

```thingsdb,json_response
[
    {
        // Replace all occurrences of `blue` with `black`
        'My favorite color is blue and I have a blue bicycle.'.replace('blue', 'black');
    },
    {
        // Replace the first occurrence of `white` with `black`
        'My favorite color is white and I have a white car.'.replace('white', 'black', 1);
    },
    {
        // Replace the last occurrence of `red` with `black`
        'My favorite color is red and I have a red mountainbike.'.replace('red', 'black', -1);
    }
]
```

> Return value in JSON format

```json
[
    "My favorite color is black and I have a black bicycle.",
    "My favorite color is black and I have a white car.",
    "My favorite color is red and I have a black mountainbike."
]
```
