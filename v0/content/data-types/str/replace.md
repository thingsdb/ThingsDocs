---
title: "replace"
weight: 108
---

Return a new [string](..) in which in which the occurrences of *old* have been replaced with *new*. Instead of an `old* string it is also possible to use a regular expression and the *new* string may also be a closure which then in turn should return a new string to replace the *old* part with.

Optionally, the *number* of replacements can be restricted and may start from either left or right *(Unless a regular expression is used, in which case the number of replacements can only be restricted from the left)*.

Param | Description
----- | -----------
groups `0..X` |
match
start position
end position



This function does *not* generate an [event](../../../overview/events).

### Function

*str*.`replace(old, new, [number])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
old | str/regex (required) | The old substring to replace, or a regular expression to search for matches.
new | str/closure (required) | String which will replace the *old* substring. If a closure is used, the return value of the closure will be used to replace the *old* substring with.
number | int (optional) | Maximum number of replacements. If not given, all occurrences of the *old* substring will be replaced. If *negative*, replacement starts at the end of the string *(a negative replacement is only possible when `old` is of type `str`)*.


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

> Example using ***replace()*** with a regular expression and capture groups: